from main import db, ma
from marshmallow import fields

class QAndAComment(db.Model):
    __tablename__ = "q_and_a_comments"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    q_and_a_id = db.Column(db.Integer, db.ForeignKey("q_and_as.id"), nullable=False)

    user = db.relationship("User", back_populates="q_and_a_comments")
    q_and_a = db.relationship("QAndA", back_populates="q_and_a_comments")
    
class QAndACommentSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "user_alias"])
    q_and_a = fields.Nested("QAndASchema", only=["id"])
    class Meta:
        fields = ("id", "description", "date", "user", "q_and_a")
        ordered = True

