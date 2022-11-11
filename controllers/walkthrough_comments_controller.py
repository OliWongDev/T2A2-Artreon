from flask import Blueprint, jsonify, request, abort
from main import db
from models.walkthrough_comments import WalkthroughComment, WalkthroughCommentSchema
from controllers.auth_controller import authorize_paid_user, authorize_general_artist
from flask_jwt_extended import jwt_required

walkthrough_comments = Blueprint("walkthrough_comments", __name__, url_prefix="/walkthrough_comments")

# 127.0.0.1:5000/walkthrough_comments
# This returns the walkthrough comments

@walkthrough_comments.route("/", methods=["GET"])
# @jwt_required()
def get_all_walkthrough_comments():
    walkthrough_comments_list = db.select(WalkthroughComment).order_by(WalkthroughComment.id.asc())
    result = db.session.scalars(walkthrough_comments_list)
    return WalkthroughCommentSchema(many=True).dump(result)

# 127.0.0.1:5000/walkthrough_comments/<int:id>
# This returns a single walkthrough comment

@walkthrough_comments.route("/<int:id>", methods=["GET"])
# @jwt_required()
def get_single_walkthrough_comment(id):
    walkthrough_comment = db.select(WalkthroughComment).filter_by(id=id)
    result = db.session.scalar(walkthrough_comment)
    return WalkthroughCommentSchema().dump(result)

# 127.0.0.1:5000/walkthrough_comments
# This adds a walkthrough comment to a walkthrough

@walkthrough_comments.route("/", methods=["POST"])
@jwt_required()
def add_walkthrough_comment():
    authorize_paid_user()
    walkthrough_comment_fields = WalkthroughCommentSchema().dump(request.json)

    new_walkthrough_comment = WalkthroughComment(
        walkthrough_id = walkthrough_comment_fields["walkthrough_id"],
        comment_id = walkthrough_comment_fields["comment_id"]
    )

    db.session.add(new_walkthrough_comment)
    db.session.commit()

    return jsonify(WalkthroughCommentSchema().dump(new_walkthrough_comment)), 201

# 127.0.0.1:5000/walkthrough_comments/<int:id>
# This updates a walkthrough comment

@walkthrough_comments.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_walkthrough_comment(id):
    authorize_paid_user()
    walkthrough_comment_data = db.select(WalkthroughCommentSchema).filter_by(id=id)
    walkthrough_comment = db.session.scalar(walkthrough_comment_data)
    if walkthrough_comment:
        walkthrough_comment.walkthrough_id = walkthrough_comment_data["walkthrough_id"],
        walkthrough_comment.comment_id = walkthrough_comment_data["comment_id"]
        db.session.commit()
        return WalkthroughCommentSchema().dump(walkthrough_comment_data)
    else:
        return abort(401, description="The walkthrough comment to be updated does not exist")

# 127.0.0.1:5000/walkthrough_comments/<int:id>
#### We want an error here telling the user that their comment needs to be deleted through the comments section

@walkthrough_comments.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_walkthrough_comment(id):
    authorize_paid_user()
    walkthrough_comment_delete_statement = db.select(WalkthroughComment).filter_by(id=id)
    walkthrough_comment = db.session.scalar(walkthrough_comment_delete_statement)
    if walkthrough_comment:
        db.session.delete(walkthrough_comment)
        db.session.commit()
        return {'message': f"Walkthrough comment with an id'{walkthrough_comment.id}' deleted successfully."}
    else:
        return {'error': f"Walkthrough comment with the id requested was not found"}, 404