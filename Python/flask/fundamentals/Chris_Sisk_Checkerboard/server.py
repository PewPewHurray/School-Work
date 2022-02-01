from random import choice
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def eight_by_eight():
    return render_template("checkerboard.html", rows = 8, columns = 8)

@app.route("/<int:x>")
def eight_by_x(x):
    return render_template("checkerboard.html", rows = x, columns = 8)

@app.route("/<int:x>/<int:y>")
def y_by_x(x, y):
    return render_template("checkerboard.html", rows = x, columns = y)

@app.route("/<int:x>/<int:y>/<string:choice1>/<string:choice2>")
def y_by_x_with_color(x, y, choice1, choice2):
    return render_template("checkerboard.html", rows = x, columns = y, color1 = choice1, color2 = choice2)

if __name__=="__main__":
    app.run(debug=True)