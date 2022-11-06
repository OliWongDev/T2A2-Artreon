from flask import Blueprint, jsonify, request
from main import db
from models.qanda_comments import QandAComment
from schemas.qanda_comment_schema import q_and_a_comment_schema, q_and_a_comments_schema

q_and_a_comments = Blueprint("qanda_comments", __name__, url_prefix="/qanda_comments")

# 127.0.0.1:5000/q_and_a_comments
# This returns the Q&A comments

q_and_a_comments.route("/", methods = ["GET"])
def get_all_q_and_as():
    q_and_a__comments_list = QandAComment.query.all()
    result = q_and_a_comments_schema.dump(q_and_a__comments_list)
    return jsonify(result)

# 127.0.0.1:5000/q_and_a_comments/<int:id>
# This returns a single Q&A comment

q_and_a_comments.route("/<int:id>", methods = ["GET"])
def get_single_q_and_a_comment(id):
    q_and_a_comment = QandAComment.query.filter_by(id=id).first()
    result = q_and_a_comment_schema.dump(q_and_a_comment)
    return jsonify(result)
