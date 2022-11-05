from main import ma

class EmailSchema(ma.Schema):
    class Meta:
        fields = ("id", "email_title", "email_content", "send_date", "artist_id")

email_schema = EmailSchema()
emails_schema = EmailSchema(many=True)