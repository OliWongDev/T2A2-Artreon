from flask import Blueprint, jsonify, request
from main import db
from models.walkthrough_comments import WalkthroughComment
from schemas.walkthrough_comment_schema import walkthrough_comment_schema, walkthrough_comments_schema

walkthrough_comments = Blueprint("walkthrough_comments", __name__, url_prefix="/walkthrough_comments")

# 127.0.0.1:5000/walkthrough_comments
# This returns the walkthrough comments

@walkthrough_comments.route("/", methods=["GET"])
def get_all_walkthrough_comments():
    walkthrough_comments_list = WalkthroughComment.query.all()
    result = walkthrough_comments_schema.dump(walkthrough_comments_list)
    return jsonify(result)

# 127.0.0.1:5000/walkthrough_comments/<int:id>
# This returns a single walkthrough comment

@walkthrough_comments.route("/<int:id>", methods=["GET"])
def get_single_walkthrough_comment(id):
    walkthrough_comment = WalkthroughComment.query.filter_by(id=id).first()
    result = walkthrough_comment_schema.dump(walkthrough_comment)
    return jsonify(result)