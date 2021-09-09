import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
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
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    stepsStringForChange = mongo.db.recipes.find_one()["steps"]
    finished = False
    unpackedStepsString = []
    while finished == False:
        num1 = stepsStringForChange.find('{space}')
        num2 = num1 + 7
        instruction = stepsStringForChange[0:num1]
        remove = stepsStringForChange[0:num2]
        unpackedStepsString.append(instruction)
        stepsStringForChange = stepsStringForChange.replace(remove, "")
        if len(stepsStringForChange) == 0:
            finished == True
            return render_template("recipes.html", recipes=recipes,
                unpackedStepsString = unpackedStepsString)
        else:
            continue



    
if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

