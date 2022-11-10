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

    artworks = db.relationship("Artwork", back_populates="artist", cascade="all, delete")
    emails = db.relationship("Email", back_populates="artist")
    q_and_as = db.relationship("QAndA", back_populates="artist", cascade="all, delete")
    walkthroughs = db.relationship("Walkthrough", back_populates="artist", cascade="all, delete")

class ArtistSchema(ma.Schema):
    artworks = fields.List(fields.Nested('ArtworkSchema'))
    emails = fields.List(fields.Nested('EmailSchema'))
    q_and_as = fields.List(fields.Nested('QAndASchema'))
    walkthroughs = fields.List(fields.Nested('WalkthroughSchema'))
    class Meta:
        fields = ("id", "artreon_alias", "password", "email", "is_admin", "artist_bio", "artworks", "emails", "q_and_as", "walkthroughs")
        ordered = True