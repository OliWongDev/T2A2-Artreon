from main import db

class Artwork(db.Model):
    __tablename__ = "artworks"
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    artwork_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    date = db.Column(db.Date(), nullable=False)
    artist_id = db.Column(db.Integer(), db.ForeignKey('artists.py'), nullable=False)