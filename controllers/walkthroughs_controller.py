from flask import Blueprint, jsonify, request, abort
from main import db
from models.walkthroughs import Walkthrough
from schemas.walkthrough_schema import walkthrough_schema, walkthroughs_schema

walkthroughs = Blueprint("walkthroughs", __name__, url_prefix="/walkthroughs")

# 127.0.0.1:5000/walkthroughs
# This returns the walkthroughs

@walkthroughs.route("/", methods=["GET"])
def get_all_walkthroughs():
    walkthroughs_list = Walkthrough.query.all()
    result = walkthroughs_schema.dump(walkthroughs_list)
    return jsonify(result)

# 127.0.0.1:5000/walkthroughs/<int:id>
# This returns a single walkthrough

@walkthroughs.route("/<int:id>", methods=["GET"])
def get_single_walkthrough(id):
    walkthrough = Walkthrough.query.filter_by(id=id).first()
    result = walkthrough_schema.dump(walkthrough)
    return jsonify(result)

# 127.0.0.1:5000/walkthroughs
# This adds a walkthrough to the database

@walkthroughs.route("/", methods=["POST"])
def add_walkthrough():

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
# This updates a walkthrough in the database

@walkthroughs.route("/<int:id>", methods=["PUT"])
def update_walkthrough(id):
    walkthrough_fields = walkthrough_schema.load(request.json)

    walkthrough = Walkthrough().query.filter_by(id=id).first()
    if not walkthrough:
        return abort(401, description="The walkthrough to be updated does not exist")
    walkthrough.description = walkthrough_fields["description"]
    walkthrough.date = walkthrough_fields["date"]
    walkthrough.artist_id = walkthrough_fields
    walkthrough.artwork_id = walkthrough_fields["artwork_id"]

    db.session.commit()

    return jsonify(walkthrough_schema.dump(walkthrough))

# 127.0.0.1:5000/walkthroughs/<int:id>
# This deletes a walkthrough in the database

@walkthroughs.route("/<int:id>", methods=["DELETE"])
def delete_walkthrough(id):

    walkthrough = Walkthrough().query.filter_by(id=id).first()
    if not walkthrough:
        return abort(401, description="The walkthrough to be deleted does not exist")
    
    db.session.delete(walkthrough)
    db.session.commit()

    return jsonify(walkthrough_schema.dump(walkthrough))


