from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def three_squares():

    return render_template("checkerboard.html", times = 3)

@app.route("/play/<int:num>")
def times_squares(num):
    
    return render_template("checkerboard.html", times = num)

@app.route("/play/<int:num>/<string:color>")
def times_squares_color(num, color):
    
    return render_template("checkerboard.html", times = num, square_color = color)

if __name__=="__main__":
    app.run(debug=True)