from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="this is the key to rule them all"

@app.route("/")
def start():

    if "visits" in session:
        session["visits"] += 1
        session["count"] += 1
    else:
        session["visits"] = 1
        session["count"] = 1

    return render_template("index.html")

@app.route("/increment", methods=["POST"])
def count_2():

    session["count"] += int(request.form["num_select"])

    return redirect("/")

@app.route("/destroy_session", methods=["POST"])
def clear():

    session.clear()

    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)