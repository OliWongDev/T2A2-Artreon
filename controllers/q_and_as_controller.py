from flask import Blueprint, jsonify, request, abort
from main import db
from models.q_and_as import QAndA
from schemas.q_and_a_schema import QAndASchema

q_and_as = Blueprint("q_and_as", __name__, url_prefix="/q_and_as")

# 127.0.0.1:5000/q_and_as
# This returns the Q&As

@q_and_as.route("/", methods = ["GET"])
def get_all_q_and_as():
    q_and_a_list = db.select(QAndA).order_by(QAndA.id.asc())
    result = db.session.scalars(q_and_a_list)
    return QAndASchema(many=True).dump(result)

# 127.0.0.1:5000/q_and_as/<int:id>
# This returns a single Q&A

@q_and_as.route("/<int:id>", methods=["GET"])
def get_single_q_and_a(id):
    q_and_a = db.select(QAndA).filter_by(id=id)
    result = db.session.scalar(q_and_a)
    return QAndASchema().dump(result)

# 127.0.0.1:5000/
#### This allows the artist to add a Q&A

@q_and_as.route("/", methods=["POST"])
def add_q_and_a():

    q_and_a_fields = q_and_a_schema.load(request.json)

    new_q_and_a = QAndA()
    new_q_and_a.q_and_a_content = q_and_a_fields["q_and_a_content"]
    new_q_and_a.date = q_and_a_fields["date"]

    db.session.add(new_q_and_a)
    db.session.commit()

    return jsonify(q_and_a_schema.dump(new_q_and_a))

# 127.0.0.1:5000/<int:id>
#### This allows an artist to update their Q&A for whatever reason they see fit.

@q_and_as.route("/<int:id>", methods=["PUT"])
def update_q_and_a(id):

    q_and_a_fields = q_and_a_schema.load(request.json)

    q_and_a = QAndA().query.filter_by(id=id).first()
    if not q_and_a:
        return abort(401, description="Q&A requested for update does not exist")
    q_and_a.content = q_and_a_fields["content"]
    q_and_a.date = q_and_a_fields["date"]

    db.session.commit()

    return jsonify(q_and_a_schema.dump(q_and_a))

# 127.0.0.1:5000/<int:id>
#### This allows an artist to delete their Q&A

@q_and_as.route("/<int:id>", methods=["DELETE"])
def delete_q_and_a(id):

    q_and_a = QAndA.query.filter_by(id=id).first()
    if not q_and_a:
        return abort(401, description="Q&A requested for deletion")

    db.session.delete(q_and_a)
    db.session.commit()

    return jsonify(q_and_a_schema.dump(q_and_a))
