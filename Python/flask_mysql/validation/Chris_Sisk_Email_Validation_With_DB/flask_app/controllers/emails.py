from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.email import Email

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/emails/add", methods=["POST"])
def create():
    
    data = {
        "email": request.form["email"]
    }
    if not Email.valid_email(data):
        return redirect("/")

    Email.create_email(data)

    return redirect("/emails")

@app.route("/emails")
def emails():

    emails = Email.get_all()

    return render_template("emails.html", emails = emails)

@app.route("/emails/<int:email_id>/destroy")
def destroy(email_id):
    data = {
        "id": email_id
    }
    Email.delete(data)
    return redirect("/emails")