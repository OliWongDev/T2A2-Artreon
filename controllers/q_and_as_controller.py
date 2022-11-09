from flask import Blueprint, jsonify, request, abort
from main import db
from models.q_and_as import QAndA, QAndASchema
from controllers.auth_controller import authorize_artist, authorize_general_artist, authorize_paid_user
from flask_jwt_extended import jwt_required

q_and_as = Blueprint("q_and_as", __name__, url_prefix="/q_and_as")

# 127.0.0.1:5000/q_and_as
# This returns the Q&As

@q_and_as.route("/", methods = ["GET"])
# @jwt_required()
def get_all_q_and_as():
    # authorize_general_artist() or authorize_general_artist()
    q_and_a_list = db.select(QAndA).order_by(QAndA.id.asc())
    result = db.session.scalars(q_and_a_list)
    return QAndASchema(many=True).dump(result)

# 127.0.0.1:5000/q_and_as/<int:id>
# This returns a single Q&A

@q_and_as.route("/<int:id>", methods=["GET"])
@jwt_required
def get_single_q_and_a(id):
    authorize_general_artist() or authorize_general_artist()
    q_and_a = db.select(QAndA).filter_by(id=id)
    result = db.session.scalar(q_and_a)
    return QAndASchema().dump(result)

# 127.0.0.1:5000/
#### This allows the artist to add a Q&A

@q_and_as.route("/", methods=["POST"])
@jwt_required()
def add_q_and_a():
    authorize_artist()
    q_and_a_fields = QAndASchema.load(request.json)
    new_q_and_a = QAndA(
        q_and_a_content = q_and_a_fields["q_and_a_content"],
        date = q_and_a_fields["date"]
    )
    db.session.add(new_q_and_a)
    db.session.commit()

    return jsonify(QAndASchema().dump(new_q_and_a)), 201


# 127.0.0.1:5000/<int:id>
#### This allows an artist to delete their Q&A

@q_and_as.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_q_and_a(id):
    authorize_artist()
    q_and_a_delete_statement = db.select(QAndA).filter_by(id=id)
    q_and_a = db.session.scalar(q_and_a_delete_statement)
    if q_and_a:
        db.session.delete(q_and_a)
        db.session.commit()
        return {'message': f"Q&A  id '{q_and_a.id}' was deleted successfully"}
    else:
        return {'error': f"The Q&A with an id '{q_and_a.id}' was not found and therefore cannot be deleted."}

