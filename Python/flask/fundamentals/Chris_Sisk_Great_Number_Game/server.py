from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "one key to rule them all"

import random           # import the random module

import sys

@app.route("/")
def start():

    session["number"]=random.randint(1, 100)  # random number between 1-100
    print(session["number"], file=sys.stderr)
    session["game_over"] = False
    session["start"] = False
    session["attempts"] = 0
    session["lose"] = False
    #session.pop("highscores")

    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def guess():

    session["attempts"] += 1
    session["start"] = True
    if int(session["number"]) == int(request.form["number"]):
        session["game_over"] = True
    elif int(session["attempts"]) == 5:
        session["game_over"] = True
        session["lose"] = True
    elif int(session["number"]) > int(request.form["number"]):
        session["low_high"] = "Low"
    else:
        session["low_high"] = "High"

    return redirect("/game")

@app.route("/game")
def game():

    return render_template("index.html")

@app.route("/highscore", methods=["POST"])
def highscore():

    if "highscores" not in session:
        session["highscores"]=[]
        session["count"]=1
    main_lst=[]
    sub_lst=[]
    if session["highscores"] != []:
        print(session["count"])
        for x in range(int(session["count"])):
            count = int(session["count"])
            main_lst.append(session["highscores"][x])
            print(main_lst, file=sys.stderr)
        count += 1
        session["count"] = count
    sub_lst.append(request.form["name"])
    sub_lst.append(session["attempts"])
    main_lst.append(sub_lst)
    session["highscores"] = main_lst
    print("highscores" + str(session["highscores"]), file=sys.stderr)

    return redirect("/leaderboard")

@app.route("/leaderboard")
def leaderboard():

    return render_template("leaderboard.html")

@app.route("/restart", methods = ["POST"])
def restart():

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)