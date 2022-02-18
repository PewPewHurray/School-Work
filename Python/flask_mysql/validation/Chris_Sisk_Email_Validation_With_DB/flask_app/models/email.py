from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    db_name = "email_validation_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        emails_from_db = connectToMySQL(cls.db_name).query_db(query)
        emails = []
        for email in emails_from_db:
            emails.append(cls(email))
        return emails

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def valid_email( data ):
        is_valid = True
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!")
            is_valid = False
        if len(Email.get_one_by_email(data)) >= 1:
            flash("Email is already in the database!")
            is_valid = False
        if is_valid == True:
            flash("The email address you entered was valid!")
        return is_valid