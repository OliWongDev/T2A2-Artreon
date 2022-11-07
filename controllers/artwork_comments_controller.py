from flask import Blueprint, jsonify, request, abort
from main import db
from models.artwork_comments import ArtworkComment
from schemas.artwork_comment_schema import artwork_comment_schema, artwork_comments_schema

artwork_comments = Blueprint('artwork_comments', __name__, url_prefix="/artwork_comments")

# 127.0.0.1:5000/artwork_comments
# This returns all the artwork comments

@artwork_comments.route("/", methods=["GET"])
def get_all_artwork_comments():
    artwork_comments_list = ArtworkComment.query.all()
    result = artwork_comments_schema.dump(artwork_comments_list)
    return jsonify(result)

# 127.0.0.1:5000/artwork_comments/<int:id>
# This returns a single artwork comment

@artwork_comments.route("/<int:id>", methods=["GET"])
def get_single_artwork_comment(id):
    artwork_comment = ArtworkComment.query.filter_by(id=id).first()
    # if not artwork_comment:
    #     return abort
    result = artwork_comment_schema.dump(artwork_comment)
    return jsonify(result)

#127.0.0.1:5000/artwork_comments
# This route allows a new artwork comment to be made to the DB
#### Authenticated + Paid User

@artwork_comments.route("/", methods=["POST"])
def add_artwork_comment():

    artwork_commment_fields = artwork_comment_schema.load(request.json)

    new_artwork_comment = ArtworkComment()
    new_artwork_comment.artwork_id = artwork_commment_fields["artwork_id"]
    new_artwork_comment.comment_id = artwork_commment_fields["comment_id"]

    db.session.add()
    db.session.commit()

    return jsonify(artwork_comment_schema.dump(new_artwork_comment))

#127.0.0.1:5000/artwork_comments/<int:id>
#### This route allows an authenticated, paid user to update their comment

@artwork_comments.route("/<int:id>", methods=["PUT"])
def update_artwork_comment(id):

    artwork_commment_fields = artwork_comment_schema.load(request.json)

    artwork_comment = ArtworkComment.query.filter_by(id=id).first()
    if not artwork_comment:
        return abort(400, description ="The artwork comment does not exist")
    artwork_comment.artwork_id = artwork_commment_fields["artwork_id"]
    artwork_comment.comment_id = artwork_commment_fields["comment_id"]

    db.session.commit()

    return jsonify(artwork_comment_schema.dump(artwork_comment))


# 127.0.0.1:5000/artwork_comments/<int:id>
#### This route allows an authenticated, paid user to delete their comment

@artwork_comments.route("/<int:id>", methods={"DELETE"})
def delete_artwork_comment(id):

    artwork_comment = ArtworkComment.query.filter_by(id=id).first()
    if not artwork_comment:
        return abort(400, description="The artwork comment does not exist")
    
    db.session.delete()
    db.session.commit()

    return jsonify(artwork_comment_schema.dump(artwork_comment))