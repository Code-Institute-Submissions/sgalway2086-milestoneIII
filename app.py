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


@app.route("/search", methods=['POST', 'GET'])
def search():
    counter = 0
    siteRecipeCount = mongo.db.recipes.find().count()
    if request.method == 'POST':
        ingredientsArray= []
        stepArray= []
        search = request.form["search_Query"]
        return redirect(url_for('searchresult', search=search))
    return render_template("search.html", counter=counter, siteRecipeCount=siteRecipeCount)


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
        print("register successful")
        print("register successful")
        print("register successful")
        print("register successful")
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=['POST', 'GET'])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        count = mongo.db.recipes.find().count()
        i = 0
        counter = 0
        titleArray = []
        imageArray = []
        descriptionArray = []
        anchorUrl = []
        recipeSet = []
        while i < count:
            currentRecipe = list(mongo.db.recipes.find())[i]
            uploader = currentRecipe["uploader"]
            if username == uploader:
                titleArray.append(currentRecipe["title"])
                imageArray.append(currentRecipe["image"])
                descriptionArray.append(currentRecipe["description"])
                anchorUrl.append(currentRecipe["_id"])
                recipeSet.append(currentRecipe)
                counter += 1
            i += 1
        return render_template('profile.html', username=username,
            recipeSet=recipeSet, titleArray=titleArray,
            imageArray=imageArray, descriptionArray=descriptionArray,
            anchorUrl=anchorUrl, counter=counter)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/deleteRecipe/<recipe_id>")
def delete_Recipe(recipe_id):
    delete = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    mongo.db.recipes.delete_one(delete)
    return redirect(url_for('profile', username=session['user']))


@app.route("/editRecipe/<recipe_id>")
def edit(recipe_id):
    edits = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    stepsStringForChange = edits.get("steps")
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
    ingredientsStringChange = edits.get("ingredients")
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
            return render_template("edits.html", edits=edits,
            unpackedStepsString=unpackedStepsString,
            unpackedIngredientsString=unpackedIngredientsString)
        else:
            continue


    return redirect(url_for('profile', username=session['user']))


@app.route("/submit", methods=['POST', 'GET'])
def test():
    if session.get("user") is not None:
        data = {}
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if request.method == "POST":
            stepsdatabase = ''
            ingredientsDataBase = ''
            steps = request.form.getlist('step')
            for i in steps:
                stepsdatabase += i + "{space}"
            print(stepsdatabase)
            ingredients = request.form.getlist('ingredient')
            for i in ingredients:
                ingredientsDataBase += i + "{space}"
            data['title'] = request.form.get('title')
            data['image'] = request.form.get('image')
            data['description'] = request.form.get('description')
            data['ingredients'] = ingredientsDataBase
            data['steps'] = stepsdatabase
            data['uploader'] = username
            mongo.db.recipes.insert_one(data)
            flash("Thank you for your submission!")
        return render_template("submit.html")
    else:
        flash("You must log in to submit a recipe")
        return render_template("login.html")


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
