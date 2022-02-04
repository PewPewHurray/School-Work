from flask import Flask, render_template, request, redirect
import sys
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form, file=sys.stderr)
    return render_template("checkout.html", strawberry=request.form["strawberry"], raspberry=request.form["raspberry"], apple=request.form["apple"],
    first_name=request.form["first_name"], last_name=request.form["last_name"], student_id=request.form["student_id"])

# When page is refreshed on the checkout page data is pulled into the page again from the from the form data

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)