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
    return render_template("recipes.html", recipes=recipes)


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)



@app.route("/unpack_String")
def unpack_String():
    description = mongo.db.recipes.description.find()
    finished = False
    stringforchange = description
    unpackedstring = []
    while finished == False:
        num1 = stringforchange.find('{space}')
        num2 = num1 + 7
        instruction = stringforchange[0:num1]
        remove = stringforchange[0:num2]
        unpackedstring.append(instruction)
        print(unpackedstring)
        stringforchange = stringforchange.replace(remove, "")
        print(stringforchange)
        if len(stringforchange) == 0:
            return render_template("recipes.html", unpackedstring = unpackedstring)
        else:
            continue
