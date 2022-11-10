from main import db, ma
from marshmallow import fields

class QAndA(db.Model):
    __tablename__ = "q_and_as"
    id = db.Column(db.Integer, primary_key=True)
    q_and_a_content = db.Column(db.String())
    date = db.Column(db.Date())

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    artists = db.relationship("Artist", back_populates="q_and_as")
    q_and_a_comments = db.relationship("QAndAComment", back_populates="q_and_as", cascade="all, delete")
    stored_questions = db.relationship("StoredQuestion", back_populates="q_and_as")


class QAndASchema(ma.Schema):
    artists = fields.Nested("ArtistSchema")
    q_and_a_comments = fields.Nested("QAndACommentSchema")
    stored_questions = fields.Nested("StoredQuestionSchema")
    class Meta:
        fields = ("id", "q_and_a_content", "date", "artist_id")
        ordered = True

