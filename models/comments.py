from main import db

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

    users = db.relationship("User", back_populates="comments")
    artwork_comments = db.relationship("ArtworkComment", back_populates="comments")
    q_and_a_comments = db.relationship("QAndAComment", back_populates="comments")
    walkthrough_comments = db.relationship("WalkthroughComment", back_populates="comments")