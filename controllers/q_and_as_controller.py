from flask import Blueprint, jsonify, request
from main import db
from models.q_and_as import QAndA
from schemas.q_and_a_schema import q_and_a_schema, q_and_as_schema

q_and_as = Blueprint("q_and_as", __name__, url_prefix="/q_and_as")

# 127.0.0.1:5000/q_and_as
# This returns the Q&As

q_and_as.route("/", methods = ["GET"])
def get_all_q_and_as():
    q_and_a_list = QAndA.query.all()
    result = q_and_as_schema.dump(q_and_a_list)
    return result

## 127.0.0.1:5000/q_and_as/<int:id>
# This returns a single Q&A

q_and_as.route("/<int>", methods=["GET"])
def get_single_q_and_a():
    q_and_a = QAndA.query.filter_by(id=id).first()
    result = q_and_a_schema.dump(q_and_a)
    return result
