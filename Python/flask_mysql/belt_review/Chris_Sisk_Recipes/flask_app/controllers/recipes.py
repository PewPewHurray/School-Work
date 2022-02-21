from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe

@app.route("/recipes/create")
def create_recipe():
    if not "id" in session:
        return redirect("/")
    return render_template("new_recipe.html")

@app.route("/recipes/add", methods=["POST"])
def add_recipe():
    data = {
        "name": request.form["recipe_name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under_30": request.form["under_30"],
        "date_made": request.form["date_made"],
        "user_id": session["id"]
    }
    if not Recipe.validate_recipe(data):
        return redirect("/recipes/create")
    Recipe.create_recipe(data)
    return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def recipe(id):
    data = {"id": id}
    recipe = Recipe.get_one_recipe_by_id(data)
    new_date_format = recipe.date_made.strftime("%B %d, %Y")
    recipe.date_made = new_date_format
    return render_template("recipe.html", recipe = recipe)

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    if not "id" in session:
        return redirect("/")
    data = {"id": id}
    recipe = Recipe.get_one_recipe_by_id(data)
    checked = {
        "checked_yes": "",
        "checked_no": ""
    }
    if recipe.under_30 == 1:
        checked["checked_yes"] = "checked"
    else:
        checked["checked_no"] = "checked"
    return render_template("edit_recipe.html", recipe = recipe, checked = checked) 

@app.route("/recipes/update/<int:id>", methods=["POST"])
def update_recipe(id):
    data = {
        "id": id,
        "name": request.form["recipe_name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"]
    }
    if not Recipe.validate_recipe(data):
        return redirect(f"/recipes/edit/{id}")
    Recipe.update_recipe_by_id(data)
    return redirect("/dashboard")

@app.route("/recipes/delete/<int:id>")
def destroy_recipe(id):
    data = {"id": id}
    Recipe.destroy_recipe_by_id(data)
    return redirect("/dashboard")