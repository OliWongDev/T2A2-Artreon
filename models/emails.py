from main import db

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email_title = db.Column(db.String(), nullable=False)
    email_content = db.Column(db.String(), nullable=False)
    send_date = db.Column(db.Date(), nullable=False)
    artist_id = db.Column(db.Integer(), db.ForeignKey("artists.id"), nullable=False)

    artist = db.relationship("Artist", back_populates="emails")