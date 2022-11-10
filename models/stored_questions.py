from main import db, ma
from marshmallow import fields

class StoredQuestion(db.Model):
    __tablename__ = "stored_questions"
    id = db.Column(db.Integer, primary_key=True)

    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    q_and_a_id = db.Column(db.Integer, db.ForeignKey("q_and_as.id"))

    questions = db.relationship("Question", back_populates="stored_questions")
    q_and_as = db.relationship("QAndA", back_populates="stored_questions")

class StoredQuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "question_id", "q_and_a_id")
        ordered = True