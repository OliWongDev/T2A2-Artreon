from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt
from models.users import User, UserSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorize_user
users = Blueprint("users", __name__, url_prefix="/users")

# 127.0.0.1:5000/users
# This returns the users

@users.route("/", methods=["GET"])
@jwt_required()
def get_all_users():
    users_list = db.select(User).order_by(User.id.asc())
    result = db.session.scalars(users_list)
    return UserSchema(many=True).dump(result)

#127.0.0.1:5000/users/<int:id>
# This returns a single user

@users.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_single_user(id):
    user = db.select(User).filter_by(id=id)
    result = db.session.scalar(user)
    return UserSchema().dump(result)

# 127.0.0.1:5000/users
# This adds a user

@users.route("/", methods=["POST"])
def add_user():
    user_fields = UserSchema().load(request.json)

    new_user = User(
    user_alias = user_fields["user_alias"],
    first_name = user_fields["first_name"],
    last_name = user_fields["last_name"],
    join_date = user_fields["join_date"],
    email = user_fields["email"],
    has_subscription = user_fields["has_subscription"],
    password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8"),
    )
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify(UserSchema().dump(new_user)), 201

# 127.0.0.1:5000/users/<int:id>
# This updates a user's details
# JWT REQUIRED
@users.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    authorize_user()
    user_data = db.select(User).filter_by(id=id)
    user = db.session.scalar(user_data)
    if user:
        user.user_alias = request.json.get('user_alias') or user.user_alias
        user.first_name = request.json.get('first_name') or user.first_name
        user.last_name = request.json.get('last_name') or user.last_name
        user.join_date = request.json.get('join_date') or user.join_date
        user.email = request.json.get('email') or user.email
        user.has_subscription = request.json.get('has_subscription')
        user.password = request.json.get('password') or user.password
        return UserSchema().dump(user)
    else:
        return abort(404, description="The user does not exist")


# 127.0.0.1:5000/users/<int:id>
# This deletes a user from the database
# JWT TOKEN REQUIRED
@users.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    authorize_user()
    user_select = db.select(User).filter_by(id=id)
    user = db.session.scalar(user_select)

    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"The user '{user.user_alias}' was deleted successfully"}
    else:
        return {'error': f"The user with the id {id} was not found to be deleted."}