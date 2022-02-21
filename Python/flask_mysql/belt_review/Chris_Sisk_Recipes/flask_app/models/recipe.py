from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name = "recipes_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.under_30 = data["under_30"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = None

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, date_made, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, (%(instructions)s), %(under_30)s, %(date_made)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod 
    def get_one_recipe_by_id(cls, data): 
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        user = results[0]["user_id"]
        recipe = cls(results[0])
        recipe.user_id = user
        return recipe

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe.user_id = row["user_id"]
            recipes.append(recipe)
        return recipes

    @classmethod
    def update_recipe_by_id(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def destroy_recipe_by_id(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters long", "recipe")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description must be at least 3 characters long", "recipe")
            is_valid = False
        if len(data["instructions"]) < 3:
            flash("Instructions must be at least 3 characters long", "recipe")
            is_valid = False
        if not data["date_made"]:
            flash("Please select a date made", "recipe")
            is_valid = False
        if not "under_30" in data:
            flash("Please select whether under 30 minutes or not", "recipe")
            is_valid = False
        return is_valid