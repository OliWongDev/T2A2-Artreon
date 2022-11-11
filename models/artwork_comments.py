from main import db, ma
from marshmallow import fields

class ArtworkComment(db.Model):
    __tablename__ = "artwork_comments"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"), nullable=False)

    user = db.relationship("User", back_populates="artwork_comments")
    artwork = db.relationship("Artwork", back_populates="artwork_comments")

class ArtworkCommentSchema(ma.Schema):
    artwork = fields.Nested("ArtworkSchema")
    comments = fields.List(fields.Nested("CommentSchema"))
    class Meta:
        fields = ("id", "artwork", "comments")
        ordered = True