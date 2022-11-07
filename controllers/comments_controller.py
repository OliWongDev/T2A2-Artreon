from flask import Blueprint, jsonify, request, abort
from main import db
from models.comments import Comment
from schemas.comment_schema import comment_schema, comments_schema

comments = Blueprint("comments", __name__, url_prefix="/comments")

# 127.0.0.1:5000/comments
# This returns the comments

@comments.route("/", methods = ["GET"])
def get_all_comments():
    comments_list = Comment.query.all()
    result = comments_schema.dump(comments_list)
    return jsonify(result)

# 127.0.0.1:5000/comments/<int:id>
# This returns a single comment

@comments.route("/<int:id>", methods=["GET"])
def get_single_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    result = comment_schema.dump(comment)
    return jsonify(result)

# 127.0.0.1:5000/comments
#### This allows a paid user to add a comment

@comments.route("/", methods=["POST"])
def add_comment():

    comment_fields = comment_schema.load(request.json)

    new_comment = Comment()
    new_comment.description = comment_fields["description"]
    new_comment.date = comment_fields["date"]
    new_comment.user_id = comment_fields["user_id"]

    db.session.add()
    db.session.commit()

    return jsonify(comment_schema.dump(new_comment))

# 127.0.0.1:5000/comments/<int:id>
#### This allows a paid user to update their comment

@comments.route("/", methods=["PUT"])
def update_comment(id):

    comment_fields = comment_schema.load(request.json)

    comment = Comment.query.filter_by(id=id).first()
    if not comment:
        return abort(400, description="This comment does not exist")
    comment.description = comment_fields["description"]
    comment.date = comment_fields["date"]
    comment.user_id = comment_fields["user_id"]

