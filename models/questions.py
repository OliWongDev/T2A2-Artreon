from main import db

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_content =db.Column(db.String(), nullable=False)
    is_answered = db.Column(db.Boolean(), nullable=False, default=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="questions")
    stored_question = db.relationship("StoredQuestion", back_populates="questions")
    