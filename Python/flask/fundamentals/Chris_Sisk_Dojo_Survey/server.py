from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.secret_key="One key to rule them all"

import sys

@app.route("/")
def start():

    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    session["first_name"]=request.form["first_name"]
    session["last_name"]=request.form["last_name"]
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    session["comment"]=request.form["comment"]
    session["color"]=request.form["color"]
    if "awesome" in request.form:
        session["awesome"]=True
    else:
        session["awesome"]=False

    return redirect("/result")

@app.route("/result")
def result():

    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)