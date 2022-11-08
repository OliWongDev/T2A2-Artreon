from flask import Blueprint, jsonify, request
from main import db
from models.stored_questions import StoredQuestion
from schemas.stored_question_schema import StoredQuestionSchema

stored_questions = Blueprint("stored_questions", __name__, url_prefix="/stored_questions")

# 127.0.0.1:5000/stored_questions
# This returns the stored_questions

@stored_questions.route("/", methods=["GET"])
def get_all_stored_questions():

    stored_questions_list = db.select(StoredQuestion).order_by(StoredQuestion.id.asc())
    result = db.session.scalars(stored_questions_list)
    return StoredQuestionSchema(many=True).dump(result)

# 127.0.0.1:5000/stored_questions/<int:id>
# This returns a single stored question

@stored_questions.route("/<int:id>", methods = ["GET"])
def get_single_stored_question(id):

    stored_question = db.select(StoredQuestion).filter_by(id=id)
    result = db.session.scalar(stored_question)
    return StoredQuestionSchema().dump(result)

# 127.0.0.1:5000/stored_questions/
# This adds a stored question

@stored_questions.route("/", methods=["POST"])
def add_stored_question():
    stored_question_fields = stored_question_schema.load(request.json)

    new_stored_question = StoredQuestion()
    new_stored_question.question_id = stored_question_fields["question_id"]
    new_stored_question.q_and_a_id = stored_question_fields["q_and_a_id"]

    db.session.add(new_stored_question)
    db.session.commit()

    return jsonify(stored_question_schema.dump(new_stored_question))