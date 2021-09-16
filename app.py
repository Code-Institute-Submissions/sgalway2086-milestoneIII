import os
import random
from flask import (
    Flask, flash, render_template, redirect, request, session, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    stepArray= []
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


def reRenderSubmit():
    return render_template('submit.html', stepArray=stepArray,
        recipeTitle=recipeTitle, url=url, shortDescription=shortDescription,
        ingredientsArray=ingredientsArray)


ingredientsArray = []
stepArray = []
@app.route('/addInfoToSite', methods=['GET','POST'])
def add_Step_Or_Ingredient():
    if request.method == "POST":
        global testIngredients
        testIngredients=request.form.get("ingredients")
        global testSteps
        testSteps = request.form.get("steps")
        global recipeTitle
        recipeTitle = request.form.get("title")
        global shortDescription
        shortDescription = request.form.get("description")
        global url
        url = request.form.get("image")
        if request.form['submit'] == 'Add Ingredient' and len(testIngredients) >= 1:
            ingredientsArray.append(request.form['ingredients'])
            return reRenderSubmit()
        elif request.form['submit'] == 'Add Step' or len(testSteps) >= 1:
            stepArray.append(request.form['steps'])
            return reRenderSubmit()
        else:
            return delete_Addition()


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    data = {}
    global stepArray
    global ingredientsArray
    if request.method == "POST":
        stepsdatabase = ''
        for i in stepArray:
            stepsdatabase += i + "{space}"
        print(stepsdatabase)
        ingredientsDataBase = ''
        for i in ingredientsArray:
            ingredientsDataBase += i + "{space}"
        print(ingredientsDataBase)
        data['title']=recipeTitle
        data['image']=url
        data['description']=shortDescription
        data['ingredients']=ingredientsDataBase
        data['steps']=stepsdatabase
        ingredientsArray= []
        stepArray= []
        mongo.db.recipes.insert_one(data)
    ingredientsArray= []
    stepArray= []
    return render_template("submit.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    counter = 0
    if request.method == 'POST':
        ingredientsArray= []
        stepArray= []
        search = request.form["search_Query"]
        return redirect(url_for('searchresult', search=search))
    return render_template("search.html", counter=counter)


@app.route('/searchresult', methods=['POST', 'GET'])
def search_Recipes():
    search = request.form.get('search_Query')
    count = mongo.db.recipes.find().count()
    i = 0
    counter = 0
    titleArray = []
    imageArray = []
    descriptionArray = []
    anchorUrl = []
    recipeSet = []
    while i < count:
        currentRecipeToCheck = list(mongo.db.recipes.find())[i]
        title = currentRecipeToCheck["title"]
        currentRecipe = list(mongo.db.recipes.find())[i]
        title = currentRecipe["title"]
        search = search.lower()
        title = title.lower()
        if search in title:
            print("TEST SUCCESS EGG")
            titleArray.append(currentRecipe["title"])
            imageArray.append(currentRecipe["image"])
            descriptionArray.append(currentRecipe["description"])
            anchorUrl.append(currentRecipe["_id"])
            recipeSet.append(currentRecipe)
            counter += 1
        i += 1
    if counter > 0:
        searchCounter = "We have found " + str(counter) + " result"
        if counter > 1:
            searchCounter += "s"
    else:
        searchCounter = "Oops, it seems we don't have that recipe"
    return render_template('search.html', search=search,
    recipeSet=recipeSet, titleArray=titleArray,
    imageArray=imageArray, descriptionArray=descriptionArray,
    anchorUrl=anchorUrl, counter=counter, searchCounter=searchCounter)


@app.route('/deleteAddition', methods=['POST', 'GET'])
def delete_Addition():
    if request.method == "POST":
        i = 0
        while i < len(stepArray):
            stepCheck = stepArray[i]
            checkDeletePoint = "delete" + stepCheck
            if request.form.get('submit') == checkDeletePoint:
                stepArray.pop(i)
                return reRenderSubmit()
            else:
                i+=1
                continue
        i = 0
        while i < len(ingredientsArray):
            ingredientsCheck = ingredientsArray[i]
            checkDeletePoint = "delete" + ingredientsCheck
            if request.form.get('submit') == checkDeletePoint:
                ingredientsArray.pop(i)
                return reRenderSubmit()
            else:
                i+=1
                continue
        return reRenderSubmit()


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
