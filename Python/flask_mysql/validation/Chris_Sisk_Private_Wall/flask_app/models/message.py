from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, redirect, request
from flask_app.models.user import User
import pprint

class Message:
    db_name = "private_wall_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = None
        self.recipient_id = None
    
    @classmethod
    def get_message_by_recipient(cls, data):
        query = "SELECT * FROM messages JOIN users ON users.id = user_id WHERE recipient_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        messages = []
        for row in results:
            message = cls(row)
            message_sender = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            sender = User(message_sender)
            message.user_id = sender
            messages.append(message)
        return messages

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE id = %(id)s;"

        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (content, created_at, updated_at, user_id, recipient_id) VALUES (%(content)s, NOW(), NOW(), %(user_id)s, %(recipient_id)s);"

        return connectToMySQL(cls.db_name).query_db(query, data)