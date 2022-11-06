from flask import Blueprint, jsonify, request
from main import db
from models.questions import Question
from schemas.question_schema import question_schema, questions_schema

questions = Blueprint("questions", __name__, url_prefix="/questions")

# 127.0.0.1:5000/questions
# This returns the questions

questions.route("/", methods=["GET"])
def get_all_questions():
    questions_list = Question.query.all()
    result = questions_schema.dump(questions_list)
    return jsonify(result)

# 127.0.0.1:5000/questions/<int:id>
# This returns a single question

questions.route("/<int:id>", methods = ["GET"])
def get_single_question(id):
    question = Question.query.filter_by(id=id).first()
    result = question_schema.dump(question)
    return jsonify(result)