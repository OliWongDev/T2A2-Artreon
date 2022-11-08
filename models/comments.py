from main import db

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

    user = db.relationship("User", back_populates="comments")
    artwork_comment = db.relationship("ArtworkComment", back_populates="comments")
    q_and_a_comment = db.relationship("QAndAComment", back_populates="comments")
    walkthrough_comment = db.relationship("WalkthroughComment", back_populates="comments")