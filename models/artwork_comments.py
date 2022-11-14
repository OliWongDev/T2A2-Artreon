from main import db, ma
from marshmallow import fields

class ArtworkComment(db.Model):
    __tablename__ = "artwork_comments"
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"), nullable=False)

    user = db.relationship("User", back_populates="artwork_comments")
    artwork = db.relationship("Artwork", back_populates="artwork_comments")

class ArtworkCommentSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "user_alias"])
    artwork = fields.Nested("ArtworkSchema", only=["id", "artwork_name"])
    class Meta:
        fields = ("id", "description", "date", "user", "artwork")
        ordered = True


# __permissions__ = dict(
#         artist_role=['post', 'read', 'delete'],
#         paid_user_role=['post', 'read', 'delete'],
#         )