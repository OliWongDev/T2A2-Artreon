from main import db, ma
from marshmallow import fields

class QAndA(db.Model):
    __tablename__ = "q_and_as"
    id = db.Column(db.Integer, primary_key=True)
    q_and_a_content = db.Column(db.String())
    date = db.Column(db.Date())

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    artist = db.relationship("Artist", back_populates="q_and_as")
    q_and_a_comments = db.relationship("QAndAComment", back_populates="q_and_as", cascade="all, delete")


class QAndASchema(ma.Schema):
    artist = fields.Nested("ArtistSchema")
    q_and_a_comment = fields.Nested("QAndACommentSchema")
    class Meta:
        fields = ("id", "q_and_a_content", "date", "artist_id", "artist", "q_and_a_comment")
        ordered = True

