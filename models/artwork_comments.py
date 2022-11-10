from main import db, ma
from marshmallow import fields

class ArtworkComment(db.Model):
    __tablename__ = "artwork_comments"
    id = db.Column(db.Integer, primary_key=True)

    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"))

    artwork = db.relationship("Artwork", back_populates="artwork_comments")
    comments = db.relationship("Comment", back_populates="artwork_comments", cascade="all, delete")

class ArtworkCommentSchema(ma.Schema):
    artwork = fields.Nested("ArtworkSchema")
    comments = fields.Nested("CommentSchema")
    class Meta:
        fields = ("id", "artwork", "comments")
        ordered = True