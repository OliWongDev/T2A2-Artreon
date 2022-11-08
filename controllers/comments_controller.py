from flask import Blueprint, jsonify, request, abort
from main import db
from models.comments import Comment
from schemas.comment_schema import CommentSchema

comments = Blueprint("comments", __name__, url_prefix="/comments")

# 127.0.0.1:5000/comments
# This returns the comments

@comments.route("/", methods = ["GET"])
def get_all_comments():
    comments_list = db.select(Comment).order_by(Comment.id.asc())
    result = db.session.scalars(comments_list)
    return CommentSchema(many=True).dump(result)

# 127.0.0.1:5000/comments/<int:id>
# This returns a single comment

@comments.route("/<int:id>", methods=["GET"])
def get_single_comment(id):
    comment = db.select(Comment).filter_by(id=id)
    result = db.session.scalar(comment)
    return CommentSchema().dump(result)

# 127.0.0.1:5000/comments
#### This allows a paid user to add a comment

@comments.route("/", methods=["POST"])
def add_comment():

    comment_fields = CommentSchema().load(request.json)

    new_comment = Comment(
        description = comment_fields["description"],
        date = comment_fields["date"],
        user_id = comment_fields["user_id"]
    )
    
    db.session.add(new_comment)
    db.session.commit()

    return jsonify(CommentSchema().dump(new_comment))

# 127.0.0.1:5000/comments/<int:id>
#### This allows a paid user to update their comment

@comments.route("/", methods=["PUT"])
def update_comment(id):

    comment_fields = comment_schema.load(request.json)

    comment = Comment.query.filter_by(id=id).first()
    if not comment:
        return abort(400, description="Comment requested to be updated does not exist")
    comment.description = comment_fields["description"]
    comment.date = comment_fields["date"]
    comment.user_id = comment_fields["user_id"]

    db.session.commit()

    return jsonify(comment_schema.dump(comment))

# 127.0.0.1:5000/comments/<int:id>
#### This allows a paid user to delete their comment

@comments.route("/<int:id>", methods=["DELETE"])
def delete_comment(id):

    comment_delete_statement = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(comment_delete_statement)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return {'message': f"Comment '{comment.description}' was deleted successfully"}
    else:  
        return {'error': f"The comment with an id '{id}' was not found and therefore cannot be deleted."}


    

