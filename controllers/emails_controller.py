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