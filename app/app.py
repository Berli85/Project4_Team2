# Import the dependencies
import numpy as np
import pandas as pd
from flask import Flask, render_template, redirect, jsonify, request
from modelHelper import ModelHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/wine_characteristics")
def wine_characteristics():
    return render_template("wine_characteristics.html")

@app.route("/around_the_world")
def around_the_world():
    return render_template("around_the_world.html")

@app.route("/about_us")
def works_cited():
    return render_template("about_us.html")

@app.route("/works_cited")
def about_us():
    return render_template("works_cited.html")


@app.route("/write_up")
def write_up():
    return render_template("write_up.html")


@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    boardgame_name = content["boardgame_name"]
    min_rating = int(content["min_rating"])
    max_owners = int(content["max_owners"])
    
    preds = modelHelper.makePredictions(boardgame_name, min_rating, max_owners)
    return(jsonify({"ok": True, "prediction":preds}))

#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# run the website
#main
if __name__ == "__main__":
    app.run(debug=True)