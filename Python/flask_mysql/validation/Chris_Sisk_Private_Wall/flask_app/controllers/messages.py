from flask_app import app
from flask_app.models.message import Message
from flask_app.models.user import User
from flask import flash, redirect, request, session

@app.route("/messages/<int:message_id>/destroy")
def destroy_message(message_id):
    data = {"id": message_id}
    Message.delete_message(data)
    return redirect("/dashboard")

@app.route("/messages/create/<int:id>", methods=["POST"])
def create_message(id):
    if len(request.form["content"]) < 5:
        flash("Messages must contain more then 4 characters")
        return redirect("/dashboard")
    data = {
        "content": request.form["content"],
        "user_id": session["id"],
        "recipient_id": id
    }
    Message.create_message(data)
    data = {"id": session["id"]}
    session["sent_count"] = User.update_sent_message_count(data)

    return redirect("/dashboard")