from main import db, ma
from marshmallow import fields

class Artwork(db.Model):
    __tablename__ = "artworks"
    id = db.Column(db.Integer, primary_key=True)
    artwork_name = db.Column(db.String(), unique=True)
    description = db.Column(db.String())
    date = db.Column(db.Date())
    artist_id = db.Column(db.Integer(), db.ForeignKey('artists.id'), nullable=False)

    artists = db.relationship("Artist", back_populates="artworks")
    artwork_comments = db.relationship("ArtworkComment", back_populates="artworks", cascade="all, delete")
    walkthroughs = db.relationship("Walkthrough", backref="artworks", cascade="all, delete")

class ArtworkSchema(ma.Schema):
    artists = fields.Nested('ArtistSchema', exclude=["password"])
    artwork_comments = fields.Nested('ArtworkCommentSchema', exclude=["artwork_id"])
    walkthroughs = fields.Nested("Walkthroughs", exclude=["artwork_id", "artist_id"])
    class Meta:
        fields = ("id", "artwork_name", "description", "date", "artists", "artwork_comments", "walkthroughs")
        ordered = True