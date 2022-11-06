from flask import Blueprint, jsonify, request
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema

users = Blueprint("users", __name__, url_prefix="/users")

# 127.0.0.1:5000/users
# This returns the users

@users.route("/", methods=["GET"])
def get_all_users():
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)

#127.0.0.1:5000/users/<int:id>
# This returns a single user

@users.route("/<int:id>", methods=["GET"])
def get_single_user():
    user = User.query.filter_by(id=id).first()
    result = user_schema.dump(user)
    return jsonify(result)