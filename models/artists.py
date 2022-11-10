from main import db, ma
from marshmallow import fields 

class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    artreon_alias = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    is_admin = db.Column(db.Boolean())
    artist_bio = db.Column(db.String())

    artworks = db.relationship("Artwork", back_populates="artists", cascade="all, delete")
    emails = db.relationship("Email", back_populates="artists")
    q_and_as = db.relationship("QAndA", back_populates="artists", cascade="all, delete")
    walkthroughs = db.relationship("Walkthrough", back_populates="artists", cascade="all, delete")

class ArtistSchema(ma.Schema):
    artworks = fields.Nested('ArtworkSchema')
    emails = fields.Nested('EmailSchema')
    q_and_as = fields.Nested('QAndASchema')
    walkthroughs = fields.Nested('WalkthroughSchema')
    class Meta:
        fields = ("id", "artreon_alias", "password", "email", "is_admin", "artist_bio", "artworks", "emails", "q_and_as", "walkthroughs")
        ordered = True