from flask import Blueprint, jsonify, request
from main import db
from models.emails import Email
from schemas.email_schema import email_schema, emails_schema

emails = Blueprint("emails", __name__, url_prefix="/emails")

# 127.0.0.1:5000/emails
# This returns the emails

@emails.route("/", methods = ["GET"])
def get_all_emails():
    emails_list = Email.query.all()
    result = emails_schema.dump(emails_list)
    return jsonify(result)

# 127.0.0.1:5000/emails/<int:id>
# This returns a single email

@emails.route("/<int:id>", methods=["GET"])
def get_single_email(id):
    email = Email.query.filter_by(id=id).first()
    result = email_schema.dump(email)
    return jsonify(result)

# 127.0.0.1:5000/
#### This allows the artist to add an email

@emails.route("/", methods=["POST"])
def add_email():

    email_fields = email_schema.load(request.json)

    new_email = Email()
    new_email.email_title = email_fields["email_title"]
    new_email.email_content = email_fields["email_content"]
    new_email.send_date = email_fields["send_date"]
    new_email.artist_id = email_fields["artist_id"]

    db.session.add()
    db.session.commit()

    return jsonify(email_schema.dump(new_email))