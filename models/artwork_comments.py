from main import db 

class ArtworkComment(db.Model):
    __tablename__ = "artwork_comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    artwork_id = db.Column(db.Integer(), db.ForeignKey("artworks.id"), nullable=False)
    comment_id = db.Column(db.Integer(), db.ForeignKey("comments.id"), nullable=False)

    artworks = db.relationship("Artwork", back_populates="artwork_comments")