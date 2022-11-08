from flask import Blueprint, jsonify, request, abort
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

# 127.0.0.1:5000/users
# This adds a user

@users.route("/", methods=["POST"])
def add_user():
    user_fields = user_schema.load(request.json)

    new_user = User()
    new_user.user_alias = user_fields["user_alias"]
    new_user.first_name = user_fields["first_name"]
    new_user.last_name = user_fields["last_name"]
    new_user.join_date = user_fields["join_date"]
    new_user.email = user_fields["email"]
    new_user.has_subscription = user_fields["has_subscription"]
    new_user.password = user_fields["password"]

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))

# 127.0.0.1:5000/users/<int:id>
# This updates a user's details

@users.route("/<int:id>", methods=["PUT"])
def update_user(id):

    user_fields = user_schema.load(request.json)

    user = User().query.filter_by(id=id).first()
    if not user:
        return abort(401, description="The user does not exist")
    user.user_alias = user_fields["user_alias"]
    user.first_name = user_fields["first_name"]
    user.last_name = user_fields["last_name"]
    user.join_date = user_fields["join_date"]
    user.email = user_fields["email"]
    user.has_subscription = user_fields["has_subscription"]
    user.password = user_fields["password"]

    db.session.commit()

    return jsonify(user_schema.dump(user))

# 127.0.0.1:5000/users/<int:id>
# This deletes a user from the database

@users.route("/<int:id>", methods=["DELETE"])
def delete_user(id):

    user = User().query.filter_by(id=id).first()
    if not user:
        abort(401, description="The user to delete does not exist")
    
    db.session.delete(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))