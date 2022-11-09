from main import db

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email_title = db.Column(db.String())
    email_content = db.Column(db.String())
    send_date = db.Column(db.Date())
    artist_id = db.Column(db.Integer(), db.ForeignKey("artists.id"))

    artists = db.relationship("Artist", back_populates="emails")