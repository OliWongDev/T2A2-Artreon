from main import db, ma
from marshmallow import fields

class Walkthrough(db.Model):
    __tablename__ = "walkthroughs"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    date = db.Column(db.Date())

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))

    artist = db.relationship("Artist", back_populates="walkthroughs")
    artwork = db.relationship("Artwork", back_populates="walkthrough")
    walkthrough_comments = db.relationship("WalkthroughComment", back_populates="walkthrough", cascade="all, delete")

class WalkthroughSchema(ma.Schema):
    artist = fields.Nested("ArtistSchema")
    artwork = fields.Nested("ArtworkSchema")
    walkthrough_comments = fields.List(fields.Nested("WalkthroughCommentSchema"))
    class Meta:
        fields = ("id", "description", "date", "artist", "artwork", "walkthrough_comments")
        ordered = True