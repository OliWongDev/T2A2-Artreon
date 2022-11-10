from main import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    date = db.Column(db.Date())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User", back_populates="comments")
    artwork_comment = db.relationship("ArtworkComment", back_populates="comments")
    q_and_a_comment = db.relationship("QAndAComment", back_populates="comments")
    walkthrough_comment = db.relationship("WalkthroughComment", back_populates="comments")

class CommentSchema(ma.Schema):
    user = fields.Nested("UserSchema")
    artwork_comment = fields.Nested("ArtworkCommentSchema"),
    q_and_a_comment = fields.Nested("QAndACommentSchema"),
    walkthrough_comment = fields.Nested("WalkthroughCommentSchema")
    class Meta:
        fields = ("id", "description", "date", "user", "artwork_comment", "q_and_a_comment", "walkthrough_comment")
        ordered = True