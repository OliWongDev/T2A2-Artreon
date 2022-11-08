from main import db

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

    users = db.relationship("User", back_populates="comments")
    artwork_comments = db.relationship("ArtworkComment", backref="parent", cascade='all, delete')
    q_and_a_comments = db.relationship("QAndAComment", backref="parent", cascade='all, delete')
    walkthrough_comments = db.relationship("WalkthroughComment", backref="parent", cascade='all, delete')