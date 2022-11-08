from main import db

class StoredQuestion(db.Model):
    __tablename__ = "stored_questions"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    q_and_a_id = db.Column(db.Integer, db.ForeignKey("q_and_as.id"), nullable=False)

    question = db.relationship("Question", back_populates="stored_questions")
    q_and_a = db.relationship("QAndA", back_populates="stored_questions")