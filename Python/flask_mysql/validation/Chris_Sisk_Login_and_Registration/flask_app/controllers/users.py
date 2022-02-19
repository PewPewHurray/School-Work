from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    if not User.validate_registration(request.form):
        return redirect("/")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }

    session["id"] = User.create(data)
    session["first_name"] = request.form["first_name"]

    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    print(user_in_db)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db[0]["password"], request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    session["id"] = user_in_db[0]["id"]
    session["first_name"] = user_in_db[0]["first_name"]
    
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if not "id" in session:
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")