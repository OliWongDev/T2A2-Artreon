from main import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_alias = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    has_subscription = db.Column(db.Boolean(), nullable=False)
    password = db.Column(db.String())

    comment = db.relationship("Comment", back_populates="users")
    question = db.relationship("Question", back_populates="users")