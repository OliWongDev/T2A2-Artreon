from main import db

class QAndA(db.Model):
    __tablename__ = "q_and_as"
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    q_and_a_content = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)