from main import db, ma
from marshmallow import fields

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email_title = db.Column(db.String(), nullable=False, unique=True)
    email_content = db.Column(db.Text, nullable=False)
    send_date = db.Column(db.Date())
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)

    artist = db.relationship("Artist", back_populates="emails")

class EmailSchema(ma.Schema):
    artist = fields.Nested("ArtistSchema", only=["id", "artreon_alias"])
    class Meta:
        fields = ("id", "email_title", "email_content", "send_date", "artist")
        ordered = True