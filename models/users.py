from main import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_alias = db.Column(db.String(), nullable=False, unique=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date())
    email = db.Column(db.String(), nullable=False, unique=True)
    has_subscription = db.Column(db.Boolean(), nullable=False, default=False)
    password = db.Column(db.String(), nullable=False)

    artwork_comments = db.relationship("ArtworkComment", back_populates="user", cascade="all, delete")
    q_and_a_comments = db.relationship("QAndAComment", back_populates="user", cascade="all, delete")
    walkthrough_comments = db.relationship("WalkthroughComment", back_populates="user", cascade="all, delete")


class UserSchema(ma.Schema):
    artwork_comments = fields.List(fields.Nested("ArtworkCommentSchema", only=["id", "description", "artwork.id", "artwork.artwork_name"]))
    q_and_a_comments = fields.List(fields.Nested("QAndACommentSchema", only=["id", "description", "q_and_a.id"]))
    walkthrough_comments = fields.List(fields.Nested("WalkthroughCommentSchema", only=["id", "description"]))
    class Meta:
        fields = ("id", "user_alias","first_name", "last_name", "join_date", "email", "has_subscription", "password", "artwork_comments", "q_and_a_comments", "walkthrough_comments")
        ordered = True