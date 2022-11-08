from main import db

class QandAComment(db.Model):
    __tablename__ = "q_and_a_comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    q_and_a_id = db.Column(db.Integer, db.ForeignKey("q_and_as.id"), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)

    q_and_a = db.relationship("QAndA", back_populates="q_and_a_comments")
    comment_id = db.relationship("Comment", back_populates="q_and_a_comments")
