from main import db, ma
from marshmallow import fields

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question_content =db.Column(db.String())
    is_answered = db.Column(db.Boolean())
    date = db.Column(db.Date())

    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))

    users = db.relationship("User", back_populates="questions")
    stored_questions = db.relationship("StoredQuestion", back_populates="questions")

class QuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "is_answered", "date", "user_id")
        ordered = True
