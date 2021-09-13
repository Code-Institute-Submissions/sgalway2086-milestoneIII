import os
import random
from flask import (
    Flask, flash, render_template, redirect, request, session, request, url_for)
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
    ingredientsArray= []
    stepsArray= []
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


stepsArray= []
@app.route('/addStepToSite', methods=['GET', 'POST'])
def step_Add():
    if request.method == 'POST':
           stepsArray.append(request.form['steps'])
    return render_template('submit.html', stepsArray=stepsArray,
                            ingredientsArray=ingredientsArray)


ingredientsArray= []
@app.route('/addIngredientToSite', methods=['GET', 'POST'])
def ingredient_Add():
    if request.method == 'POST':
           ingredientsArray.append(request.form['ingredients'])
    return render_template('submit.html', ingredientsArray=ingredientsArray,stepsArray=stepsArray)


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    data = {}
    global stepsArray
    global ingredientsArray
    if request.method == "POST":
        stepsdatabase = ''
        for i in stepsArray:
            stepsdatabase += i + "{space}"
        print(stepsdatabase)
        ingredientsDataBase = ''
        for i in ingredientsArray:
            ingredientsDataBase += i + "{space}"
        print(ingredientsDataBase)
        data['title']=request.form["title"]
        data['image']=request.form["image"]
        data['description']=request.form["description"]
        data['ingredients']=ingredientsDataBase
        data['steps']=stepsdatabase
        ingredientsArray= []
        stepsArray= []
        mongo.db.recipes.insert_one(data)
    ingredientsArray= []
    stepsArray= []
    return render_template("submit.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        ingredientsArray= []
        stepsArray= []
        search =request.form["search_Query"]
        return redirect(url_for('searchresult', search=search))
    return render_template("search.html")


@app.route('/searchresult', methods=['POST', 'GET'])
def search_Recipes():
    search=request.form.get('search_Query')
    return render_template('searchresult.html', search=search)


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


