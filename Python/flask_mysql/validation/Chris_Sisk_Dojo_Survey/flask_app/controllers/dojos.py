from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route("/")
def start():

    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    if not Dojo.validate_comment(request.form):
        return redirect("/")

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