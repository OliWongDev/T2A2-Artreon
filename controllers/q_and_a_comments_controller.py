from flask import Blueprint, jsonify, request, abort
from main import db
from models.q_and_a_comments import QandAComment
from schemas.q_and_a_comment_schema import q_and_a_comment_schema, q_and_a_comments_schema

q_and_a_comments = Blueprint("q_and_a_comments", __name__, url_prefix="/q_and_a_comments")

# 127.0.0.1:5000/q_and_a_comments
# This returns the Q&A comments

@q_and_a_comments.route("/", methods = ["GET"])
def get_all_q_and_as():
    q_and_a__comments_list = QandAComment.query.all()
    result = q_and_a_comments_schema.dump(q_and_a__comments_list)
    return jsonify(result)

# 127.0.0.1:5000/q_and_a_comments/<int:id>
# This returns a single Q&A comment

@q_and_a_comments.route("/<int:id>", methods = ["GET"])
def get_single_q_and_a_comment(id):
    q_and_a_comment = QandAComment.query.filter_by(id=id).first()
    result = q_and_a_comment_schema.dump(q_and_a_comment)
    return jsonify(result)

# 127.0.0.1:5000/q_and_a_comments/
#### This allows a paid user to add a comment to a Q&A

@q_and_a_comments.route("/", methods=["POST"])
def add_q_and_a_comment():

    q_and_a_comment_fields = q_and_a_comment_schema.load(request.json)

    new_q_and_a_comment = QandAComment()
    new_q_and_a_comment.comment_id = q_and_a_comment_fields["comment_id"]
    new_q_and_a_comment.qanda_id = q_and_a_comment_fields["qanda_id"]

    db.session.add(new_q_and_a_comment)
    db.session.commit()

    return jsonify(q_and_a_comment_schema.dump(new_q_and_a_comment))

# 127.0.0.1:5000/q_and_a_comments/<int:id>
#### This allows a paid user to update a comment to a Q&A

@q_and_a_comments.route("/<int:id>", methods=["PUT"])
def update_q_and_a_comment(id):

    q_and_a_comment_fields = q_and_a_comment_schema.load(request.json)
    q_and_a_comment = QandAComment().query.filter_by(id=id).first()
    if not q_and_a_comment:
        return abort(401, description="Q&A comment requested to be updated does not exist")
    q_and_a_comment.q_and_a_id = q_and_a_comment_fields["q_and_a_id"]

# 127.0.0.1:5000/q_and_a_comments/<int:id>
#### This allows a paid user to delete a Q&A comment

@q_and_a_comments.route("/<int:id>", methods=["DELETE"])
def delete_q_and_a_comment(id):
    
    q_and_a_comment = QandAComment().query.filter_by(id=id).first()
    if not q_and_a_comment:
        abort(401, description="Q&A comment to be deleted does not exist.")
    
    db.session.delete(q_and_a_comment)
    db.session.commit()

    return jsonify(q_and_a_comment_schema.dump(q_and_a_comment))