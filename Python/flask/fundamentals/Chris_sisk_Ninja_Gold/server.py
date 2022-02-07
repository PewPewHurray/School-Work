from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.secret_key="one key to rule them all"

import random

import sys

@app.route("/")
def main():

    #session.clear()
    if "total_gold" not in session:
        session["total_gold"] = 0
        session["moves"] = 0
        session["game_over"] = False
        session["activities"] = ["</ul>", "<ul>"]
        session["count"] = 0

    return render_template("index.html")

@app.route("/process_money", methods = ["POST"])
def process_money():

    if "restart" in request.form:
        session.clear()
        return redirect("/")
    data = request.form["property"].split()
    gold = random.randint(int(data[1]),int(data[2]))
    gamble = "earned"
    color = "text-success"
    if data[3] == "True":
        if random.choice([True, False]):
            session["total_gold"] += gold
        else:
            session["total_gold"] -= gold
            gamble = "lost"
            color = "text-danger"
    else:
        session["total_gold"] += gold
    session["moves"] += 1
    message = f"<li class='{color} fw-bold'>Entered a {data[0]} and {gamble} {gold}!</li>"
    lst = []
    for x in range(session["moves"]+1):
        lst.append(session["activities"][x])
    lst.pop()
    lst.append(message)
    lst.append("<ul>")
    session["activities"] = lst
    if int(session["total_gold"]) >= 500:
        session["game_over"] = True
        session["win_lose"] = "You Win!"
        session["color"] = "text-success"
    elif session["moves"] == 15:
        session["game_over"] = True
        session["win_lose"] = "You Lost!"
        session["color"] = "text-danger"

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)