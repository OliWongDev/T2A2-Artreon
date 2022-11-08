from main import db

class QandAComment(db.Model):
    __tablename__ = "q_and_a_comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    qanda_id = db.Column(db.Integer, db.ForeignKey("q_and_as.id"), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments_id"), nullable=False)