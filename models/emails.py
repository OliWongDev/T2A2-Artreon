from main import db, ma
from marshmallow import fields

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email_title = db.Column(db.String())
    email_content = db.Column(db.String())
    send_date = db.Column(db.Date())
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))

    artist = db.relationship("Artist", back_populates="emails")

class EmailSchema(ma.Schema):
    artists = fields.List(fields.Nested("EmailSchema"))
    class Meta:
        fields = ("id", "email_title", "email_content", "send_date", "artist")
        ordered = True