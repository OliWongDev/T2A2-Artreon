from flask import Blueprint, jsonify, request
from main import db
from models.comments import Comment
from schemas.comment_schema import comment_schema, comments_schema

comments = Blueprint("comments", __name__, url_prefix="/comments")

# 127.0.0.1:5000/comments
# This returns the comments

comments.route("/", methods = ["GET"])
def get_all_comments():
    comments_list = Comment.query.all()
    result = comments_schema.dump(comments_list)
    return result

# 127.0.0.1:5000/comments/<int:id>
# This returns a single comment

comments.route("/<int:id>", methods=["GET"])
def get_single_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    result = comment_schema.dump(comment)
    return result
