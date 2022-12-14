from main import db, ma
from marshmallow import fields

class Artwork(db.Model):
    __tablename__ = "artworks"
    __permissions__ = dict(
        artist_role=['post', 'read', 'delete', 'update'],
        paid_user_role=['read'],
        free_user_role=['read']
        )
    id = db.Column(db.Integer, primary_key=True)
    artwork_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String())
    date = db.Column(db.Date(), nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    artist = db.relationship("Artist", back_populates="artworks")
    artwork_comments = db.relationship("ArtworkComment", back_populates="artwork", cascade="all, delete")
    walkthrough = db.relationship("Walkthrough", back_populates="artwork", cascade="all, delete", uselist=False)

class ArtworkSchema(ma.Schema):
    artist = fields.Nested('ArtistSchema', only=["id", "artreon_alias"])
    artwork_comments = fields.List(fields.Nested('ArtworkCommentSchema', only=["id", "description", "user.user_alias"]))
    walkthrough = fields.Nested("WalkthroughSchema", only=["id"])
    class Meta:
        fields = ("id", "artwork_name", "description", "date", "artist", "artwork_comments", "walkthrough")
        ordered = True