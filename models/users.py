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

    comments = db.relationship("Comment", back_populates="user", cascade="all, delete")


class UserSchema(ma.Schema):
    comments = fields.List(fields.Nested("CommentSchema"))
    class Meta:
        fields = ("id", "user_alias","first_name", "last_name", "join_date", "email", "has_subscription", "password", "comments")
        ordered = True