from flask import Blueprint, jsonify, request, abort
from main import db
from models.artwork_comments import ArtworkComment
from schemas.artwork_comment_schema import ArtworkCommentSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorize_paid_user, authorize_general_artist

artwork_comments = Blueprint('artwork_comments', __name__, url_prefix="/artwork_comments")

# 127.0.0.1:5000/artwork_comments
# This returns all the artwork comments ordered by their id in descending order.

@artwork_comments.route("/", methods=["GET"])
@jwt_required()
def get_all_artwork_comments():
    authorize_paid_user() or authorize_general_artist()
    artwork_comments_list = db.select(ArtworkComment).order_by(ArtworkComment.id.desc())
    result = db.session.scalars(artwork_comments_list)
    return ArtworkCommentSchema(many=True).dump(result)

# 127.0.0.1:5000/artwork_comments/<int:id>
# This returns a single artwork comment

@artwork_comments.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_single_artwork_comment(id):
    authorize_paid_user() or authorize_general_artist()
    artwork_comment = db.select(ArtworkComment).filter_by(id=id)
    # if not artwork_comment:
    #     return abort
    result = db.session.scalar(artwork_comment)
    return ArtworkCommentSchema().dump(result)

#127.0.0.1:5000/artwork_comments
# This route allows a new artwork comment to be made to the DB
#### Authenticated + Paid User

@artwork_comments.route("/", methods=["POST"])
@jwt_required()
def add_artwork_comment():
    authorize_paid_user()
    artwork_commment_fields = ArtworkCommentSchema.load(request.json)

    new_artwork_comment = ArtworkComment(
    )
    new_artwork_comment.artwork_id = artwork_commment_fields["artwork_id"]
    new_artwork_comment.comment_id = artwork_commment_fields["comment_id"]

    db.session.add()
    db.session.commit()

    return jsonify(ArtworkCommentSchema().dump(new_artwork_comment))

#127.0.0.1:5000/artwork_comments/<int:id>
#### This route allows an authenticated, paid user to update their artwork comment

@artwork_comments.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_artwork_comment(id):
    authorize_paid_user()
    artwork_commment_fields = ArtworkCommentSchema.load(request.json)

    artwork_comment = ArtworkComment.query.filter_by(id=id).first()
    if not artwork_comment:
        return abort(400, description ="The artwork comment does not exist")
    artwork_comment.artwork_id = artwork_commment_fields["artwork_id"]
    artwork_comment.comment_id = artwork_commment_fields["comment_id"]

    db.session.commit()

    return jsonify(ArtworkCommentSchema().dump(artwork_comment))


# 127.0.0.1:5000/artwork_comments/<int:id>
#### This route allows an authenticated, paid user to delete their comment
#### We want an error here telling the user to delete the original comment
@artwork_comments.route("/<int:id>", methods={"DELETE"})
@jwt_required()
def delete_artwork_comment(id):
    authorize_paid_user
    artwork_comment = ArtworkComment.query.filter_by(id=id).first()
    if not artwork_comment:
        return abort(400, description="The artwork comment does not exist")
    
    db.session.delete(artwork_comment)
    db.session.commit()

    return jsonify(ArtworkCommentSchema().dump(artwork_comment))