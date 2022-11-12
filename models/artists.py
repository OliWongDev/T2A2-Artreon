from main import db, ma
from marshmallow import fields 


class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    artreon_alias = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)
    artist_bio = db.Column(db.String())

    artworks = db.relationship("Artwork", back_populates="artist", cascade="all, delete")
    emails = db.relationship("Email", back_populates="artist", cascade="all, delete")
    q_and_as = db.relationship("QAndA", back_populates="artist", cascade="all, delete")
    walkthroughs = db.relationship("Walkthrough", back_populates="artist", cascade="all, delete")

class ArtistSchema(ma.Schema):
    artworks = fields.List(fields.Nested('ArtworkSchema', only=["id", "artwork_name"]))
    emails = fields.List(fields.Nested('EmailSchema', only=["id", "email_title"]))
    q_and_as = fields.List(fields.Nested('QAndASchema', only=["id", "date"]))
    walkthroughs = fields.List(fields.Nested('WalkthroughSchema', only=["id", "description"]))
    class Meta:
        fields = ("id", "artreon_alias", "password", "email", "is_admin", "artist_bio", "artworks", "emails", "q_and_as", "walkthroughs")
        ordered = True