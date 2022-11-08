from flask import Blueprint, jsonify, request, abort
from main import db
from models.walkthrough_comments import WalkthroughComment
from schemas.walkthrough_comment_schema import WalkthroughCommentSchema

walkthrough_comments = Blueprint("walkthrough_comments", __name__, url_prefix="/walkthrough_comments")

# 127.0.0.1:5000/walkthrough_comments
# This returns the walkthrough comments

@walkthrough_comments.route("/", methods=["GET"])
def get_all_walkthrough_comments():
    walkthrough_comments_list = db.select(WalkthroughComment).order_by(WalkthroughComment.id.asc())
    result = db.session.scalars(walkthrough_comments_list)
    return WalkthroughCommentSchema(many=True).dump(result)

# 127.0.0.1:5000/walkthrough_comments/<int:id>
# This returns a single walkthrough comment

@walkthrough_comments.route("/<int:id>", methods=["GET"])
def get_single_walkthrough_comment(id):
    walkthrough_comment = db.select(WalkthroughComment).filter_by(id=id)
    result = db.session.scalar(walkthrough_comment)
    return WalkthroughCommentSchema().dump(result)

# 127.0.0.1:5000/walkthrough_comments
# This adds a walkthrough comment to a walkthrough

@walkthrough_comments.route("/", methods=["POST"])
def add_walkthrough_comment():

    walkthrough_comment_fields = walkthrough_comment_schema.dump(request.json)

    new_walkthrough_comment = WalkthroughComment()
    new_walkthrough_comment.walkthrough_id = walkthrough_comment_fields["walkthrough_id"]
    new_walkthrough_comment.comment_id = walkthrough_comment_fields["comment_id"]

    db.session.add(new_walkthrough_comment)
    db.session.commit()

    return jsonify(walkthrough_comment_schema.dump(new_walkthrough_comment))

# 127.0.0.1:5000/walkthrough_comments/<int:id>
# This updates a walkthrough comment

@walkthrough_comments.route("/<int:id>", methods=["PUT"])
def update_walkthrough_comment(id):

    walkthrough_comment_fields = walkthrough_comment_schema.dump(request.json)
    
    walkthrough_comment = WalkthroughComment().query.filter_by(id=id).first()
    if not walkthrough_comment:
        return abort(401, description="The walkthrough comment to be updated does not exist")
    walkthrough_comment.walkthrough_id = walkthrough_comment_fields["walkthrough_id"]
    walkthrough_comment.comment_id = walkthrough_comment_fields["comment_id"]

    db.session.commit()

    return jsonify(walkthrough_comment_schema.dump(walkthrough_comment))

# 127.0.0.1:5000/walkthrough_comments/<int:id>
# This deletes a walkthrough comment

@walkthrough_comments.route("/<int:id>", methods=["DELETE"])
def delete_walkthrough_comment(id):

    walkthrough_comment = WalkthroughComment().query.filter_by(id=id).first()
    if not walkthrough_comment:
        return abort(401, description="The walkthrough comment to be deleted does not exist")
    
    db.session.delete(walkthrough_comment)
    db.session.commit()
    
    return jsonify(walkthrough_comment_schema.dump(walkthrough_comment))