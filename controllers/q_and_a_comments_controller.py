from flask import Blueprint, jsonify, request, abort
from main import db
from models.q_and_a_comments import QAndAComment, QAndACommentSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorize_paid_user

q_and_a_comments = Blueprint("q_and_a_comments", __name__, url_prefix="/q_and_a_comments")

# 127.0.0.1:5000/q_and_a_comments
# This returns the Q&A comments

@q_and_a_comments.route("/", methods = ["GET"])
@jwt_required()
def get_all_q_and_as():
    q_and_a__comments_list = db.select(QAndAComment).order_by(QAndAComment.id.asc())
    result = db.session.scalars(q_and_a__comments_list)
    return QAndACommentSchema(many=True).dump(result)

# 127.0.0.1:5000/q_and_a_comments/<int:id>
# This returns a single Q&A comment

@q_and_a_comments.route("/<int:id>", methods = ["GET"])
@jwt_required()
def get_single_q_and_a_comment(id):
    q_and_a_comment = db.select(QAndAComment).filter_by(id=id)
    result = db.session.scalar(q_and_a_comment)
    return QAndACommentSchema().dump(result)

# 127.0.0.1:5000/q_and_a_comments/
#### This allows a paid user to add a comment to a Q&A

@q_and_a_comments.route("/", methods=["POST"])
@jwt_required()
def add_q_and_a_comment():
    authorize_paid_user()

    q_and_a_comment_fields = QAndACommentSchema.load(request.json)
    new_q_and_a_comment = QAndAComment(
        comment_id = q_and_a_comment_fields["comment_id"],
        q_and_a_id = q_and_a_comment_fields["q_and_a_id"]
    )

    db.session.add(new_q_and_a_comment)
    db.session.commit()

    return jsonify(QAndACommentSchema().dump(new_q_and_a_comment)), 201

# 127.0.0.1:5000/q_and_a_comments/<int:id>
#### This allows a paid user to update a comment to a Q&A

@q_and_a_comments.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_q_and_a_comment(id):
    authorize_paid_user()

    q_and_a_comment_data = db.select(QAndAComment).filter_by(id=id)
    q_and_a_comment = db.session.scalar(q_and_a_comment_data)
    if q_and_a_comment:
        db.session.delete(q_and_a_comment)
        db.session.commit()
        return {'message': f"Q&A comment '{q_and_a_comment.id}' was deleted successfully"}
    else:
        return abort(401, description="Q&A comment requested to be updated does not exist")

# 127.0.0.1:5000/q_and_a_comments/<int:id>
#### This allows a paid user to delete a Q&A comment
#### We want an error here telling the user that they need to delete the original comment

@q_and_a_comments.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_q_and_a_comment(id):
    authorize_paid_user()
    q_and_a_comment_data = db.select(QAndAComment).filter_by(id=id)
    q_and_a_comment = db.session.scalar(q_and_a_comment_data)
    if q_and_a_comment:
        db.session.delete(q_and_a_comment)
        db.session.commit()
        return {'message': f"Q&A comment id'{q_and_a_comment.id}' was deleted successfully"}
    else:
        return {'error': f"The comment with an id '{id}' was not found and therefore cannot be deleted."}
    