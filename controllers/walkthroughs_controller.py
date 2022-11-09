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
    walkthrough = db.select(Walkthrough).filter_by(id=id)
    result = db.session.scalar(walkthrough)
    return WalkthroughSchema().dump(result)

# 127.0.0.1:5000/walkthroughs
# This adds a walkthrough to the database

@walkthroughs.route("/", methods=["POST"])
@jwt_required()
def add_walkthrough():
    authorize_artist()
    walkthrough_fields = WalkthroughSchema().dump(request.json)
    new_walkthrough = Walkthrough(
        description = walkthrough_fields["description"],
        date = walkthrough_fields["date"],
        artist_id = walkthrough_fields["artist_id"],
        artwork_id = walkthrough_fields["artwork_id"]
    )

    db.session.add(new_walkthrough)
    db.session.commit()

    return jsonify(WalkthroughSchema().dump(new_walkthrough))

# 127.0.0.1:5000/walkthroughs/<int:id>
# This deletes a walkthrough in the database

@walkthroughs.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_walkthrough(id):
    authorize_artist()
    walkthrough_delete_statement = db.select(Walkthrough).filter_by(id=id)
    walkthrough = db.session.scalar(walkthrough_delete_statement)
    if walkthrough:
        db.session.delete(walkthrough)
        db.session.commit()
        return {'message': f"Walkthrough with an id '{walkthrough.id} was successfully deleted"}
    else:
        return {'error': "Walkthrough with the id requested was not found to be deleted."}, 404



