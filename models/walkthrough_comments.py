from main import db, ma
from marshmallow import fields

class WalkthroughComment(db.Model):
    __tablename__ = "walkthrough_comments"
    id = db.Column(db.Integer, primary_key=True)

    walkthrough_id = db.Column(db.Integer(), db.ForeignKey("walkthroughs.id"))
    comment_id = db.Column(db.Integer(), db.ForeignKey("comments.id"))

    walkthroughs = db.relationship("Walkthrough", back_populates="walkthrough_comments")
    comments = db.relationship("Comment", back_populates="walkthrough_comments", cascade="all, delete")

class WalkthroughCommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "walkthrough_id", "comment_id")
        ordered = True
