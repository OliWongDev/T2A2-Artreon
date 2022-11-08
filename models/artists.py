from main import db
# import sqlalchemy as sa

class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    artreon_alias = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean(), nullable=False)
    artist_bio = db.Column(db.String(), nullable=False)

    artworks = db.relationship("Artwork", back_populates="artists")
    emails = db.relationship("Email", back_populates="artists")
    walkthroughs = db.relationship("Walkthrough", back_populates="artists")

