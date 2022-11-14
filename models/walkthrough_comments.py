from main import db, ma
from marshmallow import fields

class WalkthroughComment(db.Model):
    __tablename__ = "walkthrough_comments"
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    walkthrough_id = db.Column(db.Integer, db.ForeignKey("walkthroughs.id"), nullable=False)

    user = db.relationship("User", back_populates="walkthrough_comments")
    walkthrough = db.relationship("Walkthrough", back_populates="walkthrough_comments")

class WalkthroughCommentSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "user_alias"])
    walkthrough = fields.Nested("WalkthroughSchema", only=["id", "description"])
    class Meta:
        fields = ("id", "description", "date", "user", "walkthrough")
        ordered = True

# __permissions__ = dict(
#         artist_role=["read"],
#         paid_user_role=["post", "read", "update", "delete"]
#     )