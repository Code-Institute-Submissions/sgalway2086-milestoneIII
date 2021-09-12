import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    recent1 = list(mongo.db.recipes.find())[-1]
    recent2 = list(mongo.db.recipes.find())[-2]
    return render_template("home.html", recent1=recent1, recent2=recent2)


@app.route("/recipes/<recipe_id>")
def get_recipes(recipe_id):
    recipes = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    stepsStringForChange = recipes.get("steps")
    stepsFinished = False
    unpackedStepsString = []
    while stepsFinished is False:
        num1 = stepsStringForChange.find('{space}')
        num2 = num1 + 7
        instruction = stepsStringForChange[0:num1]
        remove = stepsStringForChange[0:num2]
        unpackedStepsString.append(instruction)
        stepsStringForChange = stepsStringForChange.replace(remove, "")
        if len(stepsStringForChange) == 0:
            stepsFinished = True
        else:
            continue
    ingredientsStringChange = recipes.get("ingredients")
    unpackedIngredientsString = []
    ingredientsFinished = False
    while ingredientsFinished is False:
        num1 = ingredientsStringChange.find('{space}')
        num2 = num1 + 7
        instruction = ingredientsStringChange[0:num1]
        remove = ingredientsStringChange[0:num2]
        unpackedIngredientsString.append(instruction)
        ingredientsStringChange = ingredientsStringChange.replace(remove, "")
        if len(ingredientsStringChange) == 0:
            ingredientsFinished = True
            return render_template("recipes.html", recipes=recipes,
            unpackedStepsString=unpackedStepsString,
            unpackedIngredientsString=unpackedIngredientsString)
        else:
            continue


@app.route("/randomrecipe")
def random_recipe():
    totalRecipes = mongo.db.recipes.count_documents({})
    totalRecipes -= 1
    randomRecipe = random.randint(0, totalRecipes)
    numberOnDb = list(mongo.db.recipes.find())[randomRecipe]
    numberOnDb = numberOnDb.get('_id')
    return get_recipes(numberOnDb)


@app.route("/submit")
def submit():
    return render_template("submit.html")


@app.route("/search")
def search():
    return render_template("search.html")


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


@app.route('/searchresult', methods=['POST', 'GET'])
def search_Recipes():
    if request.method == 'POST':
        search = request.form['search_Query']
        return search
    return render_template('searchresult.html', search=search)
