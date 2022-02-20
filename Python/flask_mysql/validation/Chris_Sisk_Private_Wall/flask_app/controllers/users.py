from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "id" in session:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/users/add", methods=["POST"])
def add_user():
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
    session["sent_count"] = 0

    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db[0]["password"], request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    session["id"] = user_in_db[0]["id"]
    session["first_name"] = user_in_db[0]["first_name"]
    session["sent_count"] = User.get_sent_count(session)[0]["sent_message_count"]
    print(session["sent_count"])
    
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if not "id" in session:
        return redirect("/")
    data = {
        "id": session["id"]
    }
    messages = Message.get_message_by_recipient(data)
    time_ago = ""
    count = 0
    message_count = "You have no messages"
    if len(messages) > 0:
        count = len(messages)
        created = messages[0].created_at
        current = datetime.datetime.now().replace(microsecond=0)
        difference = str(current-created)
        if "," in difference:
            difference1 = difference.split(", ")
            time_ago = difference1[0]
        else:
            difference1 = difference.split(":")
            if difference1[0] != "0":
                hours = difference1[0]
                check = " hours"
                if hours == "1":
                    check = " hour"
                time_ago = (hours + check)
            elif difference1[1] != "00":
                minutes = int(difference1[1])
                check = " minutes"
                if minutes == 1:
                    check = " minute"
                time_ago = (str(minutes) + check)
            else:
                seconds = int(difference1[2])
                check = " seconds"
                if seconds == 1:
                    check = " second"
                time_ago = (str(seconds) + check)
    if count != 0:
        message_count = f"You have {count} messages"
    users = User.get_all_except_current(data)
    users = sorted(users, key=lambda item: item.first_name)

    return render_template("dashboard.html", messages = messages, time = time_ago, users = users, message_count = message_count)

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")