from main import db

class Artwork(db.Model):
    __tablename__ = "artworks"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    artwork_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    date = db.Column(db.Date(), nullable=False)
    artist_id = db.Column(db.Integer(), db.ForeignKey('artists.id'), nullable=False)

    artists = db.relationship("Artist", back_populates="artworks")
    artwork_comments = db.relationship("ArtworkComment", back_populates="artworks")
    walkthroughs = db.relationship("Walkthrough", back_populates="artworks")