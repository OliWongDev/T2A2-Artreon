from flask import Blueprint, jsonify, request, abort
from main import db
from models.questions import Question
from schemas.question_schema import QuestionSchema
from controllers.auth_controller import authorize_paid_user, authorize_general_artist
from flask_jwt_extended import jwt_required

questions = Blueprint("questions", __name__, url_prefix="/questions")

# 127.0.0.1:5000/questions
# This returns the questions

@questions.route("/", methods=["GET"])
@jwt_required()
def get_all_questions():
    authorize_general_artist() or authorize_paid_user()
    questions_list = db.select(Question).order_by(Question.id.asc())
    result = db.session.scalars(questions_list)
    return QuestionSchema(many=True).dump(result)

# 127.0.0.1:5000/questions/<int:id>
# This returns a single question

@questions.route("/<int:id>", methods = ["GET"])
@jwt_required()
def get_single_question(id):
    authorize_general_artist() or authorize_paid_user
    question = db.select(Question).filter_by(id=id)
    result = db.session.scalar(question)
    return QuestionSchema().dump(result)

# 127.0.0.1:5000/questions
# This allows the user to post/add a question to the database

@questions.route("/", methods=["POST"])
@jwt_required()
def add_question():
    authorize_paid_user()
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
@jwt_required()
def update_question(id):
    authorize_paid_user()
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
@jwt_required
def delete_question(id):
    authorize_paid_user
    question = Question().query.filter_by(id=id).first()
    if not question:
        abort(401, description="The question to be deleted does not exist.")
    
    db.session.delete(question)
    db.session.commit()

    return jsonify(question_schema.dump(question))