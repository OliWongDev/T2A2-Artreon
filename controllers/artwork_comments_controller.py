from flask import Blueprint, jsonify, request
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

