from flask import Blueprint, jsonify, request, abort
from main import db
from models.questions import Question
from schemas.question_schema import question_schema, questions_schema

questions = Blueprint("questions", __name__, url_prefix="/questions")

# 127.0.0.1:5000/questions
# This returns the questions

@questions.route("/", methods=["GET"])
def get_all_questions():
    questions_list = Question.query.all()
    result = questions_schema.dump(questions_list)
    return jsonify(result)

# 127.0.0.1:5000/questions/<int:id>
# This returns a single question

@questions.route("/<int:id>", methods = ["GET"])
def get_single_question(id):
    question = Question.query.filter_by(id=id).first()
    result = question_schema.dump(question)
    return jsonify(result)

# 127.0.0.1:5000/questions
# This allows the user to post/add a question to the database

@questions.route("/", methods=["POST"])
def add_question():
    question_fields = question_schema.load(request.json)

    new_question = Question()
    new_question.question_content = question_fields["question_content"]
    new_question.is_answered = question_fields["is_answered"]
    new_question.date = question_fields["date"]
    new_question.user_id = question_fields["user_id"]

    db.session.add(new_question)
    db.session.commit()

    return jsonify(question_fields.dump(new_question))

# 127.0.0.1:5000/questions/<int:id>
# This allows the user to update a question they have made

questions.route("/<int:id>", methods=["PUT"])
def update_question(id):

    question_fields = question_schema.load(request.json)
    
    question = Question().query.filter_by(id=id).first()
    if not question:
        return abort(401, description="The question to be updated does not exist")
    question.question_content = question_fields["question_content"]
    question.is_answered = question_fields["is_answered"]
    question.date = question_fields["date"]
    question.user_id = question_fields["user_id"]

    db.session.commit()

    return jsonify(question_fields.dump(question))

# 127.0.0.1:5000/questions/<int:id>
# This allows the user to delete a question they have made

questions.route("/<int:id>", methods=["DELETE"])
def delete_question(id):

    question = Question().query.filter_by(id=id).first()
    if not question:
        abort(401, description="The question to be deleted does not exist.")
    
    db.session.delete(question)
    db.session.commit()

    return jsonify(question_schema.dump(question))