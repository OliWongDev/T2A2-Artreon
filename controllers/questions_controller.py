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
    question_fields = QuestionSchema().load(request.json)

    new_question = Question(
        question_content = question_fields["question_content"],
        question_content = question_fields["date"],
        user_id = question_fields["user_id"]
    )

    db.session.add(new_question)
    db.session.commit()

    return jsonify(QuestionSchema().dump(new_question))

# 127.0.0.1:5000/questions/<int:id>
# This allows the user to update a question they have made

questions.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_question(id):
    authorize_paid_user()
    question_fields = db.select(QuestionSchema).filter_by(id=id)
    question = db.session.scalar(question_fields)

    if question:
        question.question_content = request.json.get("question_content")
        question.is_answered = request.json.get("is_answered")
        question.date = request.json.get("date")
        question.user_id = request.json.get("user_id")
        db.session.commit()
        return QuestionSchema().dump(question)
    else:
        return abort(401, description="The question to be updated does not exist")

# 127.0.0.1:5000/questions/<int:id>
# This allows the user to delete a question they have made

questions.route("/<int:id>", methods=["DELETE"])
@jwt_required
def delete_question(id):
    authorize_paid_user
    question_delete_statement = db.select(QuestionSchema).filter_by(id=id)
    question = db.session.scalar(question_delete_statement)
    if question:
        db.session.delete(question)
        db.session.commit()
        return {'message': f"Question '{question.question_content}' was deleted successfully"}
    else:
        abort(401, description="The question to be deleted does not exist.")
    
 