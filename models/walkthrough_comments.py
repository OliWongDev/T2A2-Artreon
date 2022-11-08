from main import db

class WalkthroughComment(db.Model):
    __tablename__ = "walkthrough_comments"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    walkthrough_id = db.Column(db.Integer(), db.ForeignKey("walkthroughs.id"), nullable=False)
    comment_id = db.Column(db.Integer(), db.ForeignKey("comments.id"), nullable=False)

    walkthroughs = db.relationship("Walkthrough", back_populates="walkthrough_comments")
