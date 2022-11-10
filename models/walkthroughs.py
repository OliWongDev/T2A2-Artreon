from main import db, ma
from marshmallow import fields

class Walkthrough(db.Model):
    __tablename__ = "walkthroughs"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    date = db.Column(db.Date())

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))

    artists = db.relationship("Artist", back_populates="walkthroughs")
    artworks = db.relationship("Artwork", back_populates="walkthroughs")
    walkthrough_comments = db.relationship("WalkthroughComment", back_populates="walkthroughs", cascade="all, delete")

class WalkthroughSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "date", "artist_id", "artwork_id")
        ordered = True