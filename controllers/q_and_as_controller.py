from flask import Blueprint, jsonify, request, abort
from main import db
from models.q_and_as import QAndA, QAndASchema
from models.q_and_a_comments import QAndAComment, QAndACommentSchema
from controllers.auth_controller import authorize_artist, authorize_paid_user, authorize_precise_user
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime
from models.q_and_a_comments import QAndAComment, QAndACommentSchema

q_and_as = Blueprint("q_and_as", __name__, url_prefix="/qandas")

# 127.0.0.1:5000/q_and_as
# This returns the Q&As

@q_and_as.route("/", methods = ["GET"])
# @jwt_required()
def get_all_q_and_as():
    # user_id = get_jwt_identity()
    # authorize_paid_user(user_id)
    q_and_a_list = db.select(QAndA).order_by(QAndA.id.asc())
    result = db.session.scalars(q_and_a_list)
    return QAndASchema(many=True).dump(result)

# 127.0.0.1:5000/q_and_as/<int:id>
# This returns a single Q&A

@q_and_as.route("/<int:id>", methods=["GET"])
# @jwt_required
def get_single_q_and_a(id):
    # authorize_general_artist() or authorize_general_artist()
    q_and_a = db.select(QAndA).filter_by(id=id)
    result = db.session.scalar(q_and_a)
    return QAndASchema().dump(result)

# 127.0.0.1:5000/
#### This allows the artist to add a Q&A

@q_and_as.route("/", methods=["POST"])
# jwt_required()
def add_q_and_a():
    q_and_a_fields = QAndASchema().load(request.json)
    new_q_and_a = QAndA(
        q_and_a_content = q_and_a_fields["q_and_a_content"],
        date = datetime.date.today(),
        artist_id = 1
    )
    db.session.add(new_q_and_a)
    db.session.commit()

    return QAndASchema().dump(new_q_and_a), 201

# 127.0.0.1:5000/q_and_as/<int:id>
# Allows artist to update Q&A

@q_and_as.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_q_and_a(id):
    q_and_a_fields = db.select(QAndA).filter_by(id=id)
    q_and_a = db.session.scalar(q_and_a_fields)
    authorize_artist(get_jwt_identity())
    if q_and_a: 
        q_and_a.q_and_a_content = request.json.get('q_and_a_content') or q_and_a.q_and_a_content,
        q_and_a.date = datetime.date.today()
        db.session.commit()
        return QAndASchema().dump(q_and_a)
    else:
        return {"error": f"Q&A not found with id {id}"}, 404

# 127.0.0.1:5000/q_and_as/<int:id>
#### This allows an artist to delete their Q&A

@q_and_as.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_q_and_a(id):
    # authorize_artist()
    q_and_a_delete_statement = db.select(QAndA).filter_by(id=id)
    q_and_a = db.session.scalar(q_and_a_delete_statement)
    if q_and_a:
        db.session.delete(q_and_a)
        db.session.commit()
        return {'message': f"Q&A  id '{q_and_a.id}' was deleted successfully"}
    else:
        return {'error': f"The Q&A with an id '{q_and_a.id}' was not found and therefore cannot be deleted."}

# 127.0.0.1:5000/q_and_as/<int:id>/comments
# Post a comment for a particular Q&A
# DO NOT TOUCH
@q_and_as.route("/<int:q_and_a_id>/comments", methods=["POST"])
@jwt_required()
def create_q_and_a_comment(q_and_a_id):
    q_and_a_statement = db.select(QAndA).filter_by(id=q_and_a_id)
    q_and_a = db.session.scalar(q_and_a_statement)
    authorize_paid_user(get_jwt_identity())
    if q_and_a:
        q_and_a_comment = QAndAComment(
            description = request.json['description'],
            date = datetime.date.today(),
            user_id = get_jwt_identity(),
            q_and_a_id = q_and_a_id
        )
        db.session.add(q_and_a_comment)
        db.session.commit()
        return QAndACommentSchema().dump(q_and_a_comment), 201
    else:
        {'error': f"Q&A not found with id '{id}'"}, 404

@q_and_as.route("/<int:id>/comments/<int:q_and_a_comment_id>", methods = ["PUT", "PATCH"])
@jwt_required()
def update_q_and_a_comment(id, q_and_a_comment_id):
     q_and_a_statement = db.select(QAndA).filter_by(id=id)
     q_and_a = db.session.scalar(q_and_a_statement)
     q_and_a_comment_statement = db.select(QAndAComment).filter_by(id=q_and_a_comment_id)
     q_and_a_comment = db.session.scalar(q_and_a_comment_statement)
     authorize_precise_user(q_and_a_comment.user_id)
     if q_and_a and q_and_a_comment:
          q_and_a_comment.description = request.json.get('description') or q_and_a_comment.description
          db.session.commit()
          return QAndACommentSchema().dump(q_and_a_comment), 201
     elif q_and_a: 
          return {'error': f"Q&A was not found with id {id}"}


@q_and_as.route("/<int:id>/comments/<int:q_and_a_comment_id>", methods = ["DELETE"])
@jwt_required()
def delete_q_and_a_comment(id, q_and_a_comment_id):
     q_and_a_statement = db.select(QAndA).filter_by(id=id)
     q_and_a = db.session.scalar(q_and_a_statement)
     q_and_a_comment_statement = db.select(QAndAComment).filter_by(id=q_and_a_comment_id)
     q_and_a_comment = db.session.scalar(q_and_a_comment_statement)
     authorize_precise_user(q_and_a_comment.user_id)

     if q_and_a and q_and_a_comment:
          db.session.delete(q_and_a_comment)
          db.session.commit()
          return {'message': f"QAndA comment deleted successfully"}
     elif q_and_a: 
          return {'error': f"Artwork Comment not found with id {id}"}, 404
     elif q_and_a_comment:
          return {'error': f"Artwork was not found on artwork '{id}'."}, 404
