from flask import Blueprint, jsonify, request
from main import db
from models.emails import Email, EmailSchema
from controllers.auth_controller import authorize_artist
from flask_jwt_extended import jwt_required

emails = Blueprint("emails", __name__, url_prefix="/emails")

# 127.0.0.1:5000/emails
# This returns the emails

@emails.route("/", methods = ["GET"])
#jwt_required()
def get_all_emails():
    emails_list = db.select(Email).order_by(Email.id.asc())
    result = db.session.scalars(emails_list)
    return EmailSchema(many=True).dump(result)

# 127.0.0.1:5000/emails/<int:id>
# This returns a single email

@emails.route("/<int:id>", methods=["GET"])
# @jwt_required()
def get_single_email(id):
    email = db.select(Email).filter_by(id=id)
    result = db.session.scalar(email)
    return EmailSchema().dump(result)

# 127.0.0.1:5000/
#### This allows the artist to add an email

@emails.route("/", methods=["POST"])
@jwt_required()
def add_email():
    authorize_artist()
    email_fields = EmailSchema().load(request.json)

    new_email = Email(
    email_title = email_fields["email_title"],
    email_content = email_fields["email_content"],
    send_date = email_fields["send_date"],
    artist_id = email_fields["artist_id"])

    db.session.add(new_email)
    db.session.commit()

    return jsonify(EmailSchema().dump(new_email)), 201