from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name = "private_wall_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.sent_message_count = 0
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"

        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_except_current(cls, data):
        query = "SELECT * FROM users WHERE id <> %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_sent_count(cls, data):
        query = "SELECT sent_message_count FROM users Where id = %(id)s;"

        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_sent_message_count(cls, data):
        count = (int(User.get_sent_count(data)[0]["sent_message_count"]))
        count = count + 1
        data["count"] = count
        query = "UPDATE users SET sent_message_count = %(count)s WHERE id = %(id)s;"
        connectToMySQL(cls.db_name).query_db(query, data)
        return count



    @staticmethod
    def validate_registration(data):
        is_valid = True
        valid_password = True
        if len(data["first_name"]) < 3:
            flash("First name must be at least 2 characters long", "registration")
            is_valid = False
        if len(data["last_name"]) < 3:
            flash("Last name must be at least 2 characters long", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Not a valid email address", "registration")
            is_valid = False
        weak_passwords = ['LetMeIn1!', "Password123!", "Opensesame1!"]
        if data["password"] in weak_passwords:
            flash("Please pick a strong password", "registration")
            valid_password = False
        if len(data["password"]) < 8:
            flash("Password is too short", "registration")
            valid_password = False
        if data["password"].isalnum():
            flash("Password is missing a special character", "registration")
            valid_password = False
        if data["password"].islower():
            flash("Password is missing a uppercase letter", "registration")
            valid_password = False
        if data["password"].isupper():
            flash("Password is missing a lowercase letter", "registration")
            valid_password = False
        num_test = False
        letter_test = False
        for x in data["password"]:
            if x.isdigit():
                num_test = True
                if letter_test:
                    break
            elif x.isalnum():
                letter_test = True
        if not letter_test:
            flash("Password needs a uppercase and lowercase letter", "registration")
            valid_password = False
        if not num_test:
            flash("Password is missing a number", "registration")
            valid_password = False
        if valid_password:
            if data["password"] != request.form["confirm_password"]:
                flash("Passwords do not match", "registration")
                is_valid = False
        return is_valid