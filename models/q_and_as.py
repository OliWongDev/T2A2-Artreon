from main import db

class QAndA(db.Model):
    __tablename__ = "q_and_as"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    q_and_a_content = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)

    q_and_a_comments = db.relationship("QAndAComment", back_populates='q_and_as')
    stored_questions = db.relationship("StoredQuestion", back_populates='q_and_as')

