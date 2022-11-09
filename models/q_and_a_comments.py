from main import db

class QAndAComment(db.Model):
    __tablename__ = "q_and_a_comments"
    id = db.Column(db.Integer, primary_key=True)

    q_and_a_id = db.Column(db.Integer(), db.ForeignKey("q_and_as.id"))
    comment_id = db.Column(db.Integer(), db.ForeignKey("comments.id"))

    q_and_as = db.relationship("QAndA", back_populates="q_and_a_comments")
    comments = db.relationship("Comment", back_populates="q_and_a_comments", cascade="all, delete")

