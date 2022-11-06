from flask import Blueprint, jsonify, request
from main import db
from models.stored_questions import StoredQuestion
from schemas.stored_question_schema import stored_question_schema, stored_questions_schema

stored_questions = Blueprint("stored_questions", __name__, url_prefix="/stored_questions")

# 127.0.0.1:5000/stored_questions
# This returns the stored_questions

@stored_questions.route("/", methods=["GET"])
def get_all_stored_questions():
    stored_questions_list = StoredQuestion.query.all()
    result = stored_questions_schema.dump(stored_questions_list)
    return jsonify(result)

# 127.0.0.1:5000/stored_questions/<int:id>
# This returns a single stored question

@stored_questions.route("/<int:id>", methods = ["GET"])
def get_single_stored_question(id):
    stored_question = StoredQuestion.query.filter_by(id=id).first()
    result = stored_question_schema.dump(stored_question)
    return jsonify(result)
