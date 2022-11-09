from flask import Blueprint, jsonify, request, abort
from main import db
from models.comments import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorize_paid_user


comments = Blueprint("comments", __name__, url_prefix="/comments")

# 127.0.0.1:5000/comments
# This returns the comments

@comments.route("/", methods = ["GET"])
@jwt_required()
def get_all_comments():
    comments_list = db.select(Comment).order_by(Comment.id.asc())
    result = db.session.scalars(comments_list)
    return CommentSchema(many=True).dump(result)

# 127.0.0.1:5000/comments/<int:id>
# This returns a single comment

@comments.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_single_comment(id):
    comment = db.select(Comment).filter_by(id=id)
    result = db.session.scalar(comment)
    return CommentSchema().dump(result)

# 127.0.0.1:5000/comments
#### This allows a paid user to add a comment

@comments.route("/", methods=["POST"])
@jwt_required()
def add_comment():
    authorize_paid_user()
    comment_fields = CommentSchema().load(request.json)

    new_comment = Comment(
        description = comment_fields["description"],
        date = comment_fields["date"],
        user_id = get_jwt_identity()
    )
    
    db.session.add(new_comment)
    db.session.commit()

    return jsonify(CommentSchema().dump(new_comment)), 201

# 127.0.0.1:5000/comments/<int:id>
#### This allows a paid user to update their comment

@comments.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_comment(id):
    authorize_paid_user()
    comment_data = db.select(Comment).filter_by(id=id)

    comment = db.session.scalar(comment_data)
    if comment:
        comment.description = request.json.get('description')
        comment.date = request.json.get('date')
        db.session.commit()
        return CommentSchema().dump(comment)
    else:
        return abort(400, description="Comment requested to be updated does not exist")

# 127.0.0.1:5000/comments/<int:id>
#### This allows a paid user to delete their comment

@comments.route("/<int:id>", methods=["DELETE"])
@jwt_required
def delete_comment(id):
    authorize_paid_user()
    comment_delete_statement = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(comment_delete_statement)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return {'message': f"Comment '{comment.description}' was deleted successfully"}
    else:  
        return {'error': f"The comment with an id '{id}' was not found and therefore cannot be deleted."}


    

