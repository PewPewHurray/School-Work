from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db_name = "dojo_survey_schema"

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        return connectToMySQL(db_name).query_db(query)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW() , NOW());"
        return connectToMySQL(db_name).query_db(query, data)

    @staticmethod
    def validate_comment(data):
        is_valid = True # we assume this is true
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if data['location'] == "":
            flash("Must select a location.")
            is_valid = False
        if data['language'] == "":
            flash("Must select a language.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("Comment must be at least 3 characters.")
        return is_valid