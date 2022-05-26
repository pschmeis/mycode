#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

questionbank = [{
        "prompt" : "What is your quest?", 
        "answer" : "To seek the holy grail" 
    },
    {   
        "prompt" : "What is the airspeed velocity of an unladen swallow?",
        "answer" : "African or European"
    },
    {
        "prompt" : "What is your favorite color",
        "answer" : "red"
    }
             ]
@app.route("/questions")
def questions():
    return jsonify(questionbank)

# This is a landing point for users (a start)
#@app.route("/") # user can land at "/"
#def start():
#    return render_template("trivia.html")
# This is where postmaker.html POSTs data to
@app.route("/", methods = ["GET", "POST"])
def trivia():
    if request.method == "GET":
        return render_template("trivia.html")
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        return render_template("trivia.html", ans = request.form.get("nm").lower())
    
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

