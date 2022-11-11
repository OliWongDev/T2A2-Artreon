from main import db, ma
from marshmallow import fields

class QAndA(db.Model):
    __tablename__ = "q_and_as"
    id = db.Column(db.Integer, primary_key=True)
    q_and_a_content = db.Column(db.String(), nullable=False, unique=True)
    date = db.Column(db.Date(), nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    artist = db.relationship("Artist", back_populates="q_and_as")
    q_and_a_comments = db.relationship("QAndAComment", back_populates="q_and_a", cascade="all, delete")


class QAndASchema(ma.Schema):
    artist = fields.Nested("ArtistSchema", only=["id", "artreon_alias"])
    q_and_a_comments = fields.List(fields.Nested("QAndACommentSchema", only=["id", "description", "user.user_alias"]))
    class Meta:
        fields = ("id", "q_and_a_content", "date", "artist", "q_and_a_comments")
        ordered = True

