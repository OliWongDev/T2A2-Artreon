from main import db

class Walkthrough(db.Model):
    __tablename__ = "walkthroughs"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String())
    date = db.Column(db.Date(), nullable=False)
    artist_id = db.Column(db.Integer(), db.ForeignKey("artists.id"))
    artwork_id = db.Column(db.Integer(), db.ForeignKey("artworks.id"), nullable=False)

    artist = db.relationship("Artist", back_populates="walkthroughs")
    artwork = db.relationship("Artwork", back_populates="walkthroughs")
    walkthrough_comment = db.relationship("WalkthroughComment", back_populates="walkthroughs")