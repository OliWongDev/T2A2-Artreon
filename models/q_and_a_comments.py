from main import db, ma
from marshmallow import fields

class QAndAComment(db.Model):
    __tablename__ = "q_and_a_comments"
    id = db.Column(db.Integer, primary_key=True)

    q_and_a_id = db.Column(db.Integer(), db.ForeignKey("q_and_as.id"))
    comment_id = db.Column(db.Integer(), db.ForeignKey("comments.id"))

    q_and_as = db.relationship("QAndA", back_populates="q_and_a_comments")
    comments = db.relationship("Comment", back_populates="q_and_a_comments", cascade="all, delete")

class QAndACommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "q_and_a_id", "comment_id")
        ordered = True

