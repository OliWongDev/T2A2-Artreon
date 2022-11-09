from flask import Blueprint, jsonify, request, abort
from main import db
from models.walkthroughs import Walkthrough
from schemas.walkthrough_schema import WalkthroughSchema
from controllers.auth_controller import authorize_artist, authorize_paid_user, authorize_general_artist
from flask_jwt_extended import jwt_required

walkthroughs = Blueprint("walkthroughs", __name__, url_prefix="/walkthroughs")

# 127.0.0.1:5000/walkthroughs
# This returns the walkthroughs

@walkthroughs.route("/", methods=["GET"])
@jwt_required()
def get_all_walkthroughs():
    authorize_general_artist() or authorize_paid_user()
    walkthroughs_list = db.select(Walkthrough).order_by(Walkthrough.id.asc())
    result = db.session.scalars(walkthroughs_list)
    return WalkthroughSchema(many=True).dump(result)

# 127.0.0.1:5000/walkthroughs/<int:id>
# This returns a single walkthrough

@walkthroughs.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_single_walkthrough(id):
    authorize_general_artist() or authorize_paid_user()
    walkthrough = Walkthrough.query.filter_by(id=id).first()
    result = walkthrough_schema.dump(walkthrough)
    return jsonify(result)

# 127.0.0.1:5000/walkthroughs
# This adds a walkthrough to the database

@walkthroughs.route("/", methods=["POST"])
@jwt_required()
def add_walkthrough():
    authorize_artist()
    walkthrough_fields = walkthrough_schema.load(request.json)

    new_walkthrough = Walkthrough()
    new_walkthrough.description = walkthrough_fields["description"]
    new_walkthrough.date = walkthrough_fields["date"]
    new_walkthrough.artist_id = walkthrough_fields["artist_id"]
    new_walkthrough.artwork_id = walkthrough_fields["artwork_id"]

    db.session.add(new_walkthrough)
    db.session.commit()

    return jsonify(walkthrough_schema.dump(new_walkthrough))

# 127.0.0.1:5000/walkthroughs/<int:id>
# This deletes a walkthrough in the database

@walkthroughs.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_walkthrough(id):
    authorize_artist()
    walkthrough = Walkthrough().query.filter_by(id=id).first()
    if not walkthrough:
        return abort(401, description="The walkthrough to be deleted does not exist")
    
    db.session.delete(walkthrough)
    db.session.commit()

    return jsonify(walkthrough_schema.dump(walkthrough))


