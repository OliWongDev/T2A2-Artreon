from flask import Blueprint, jsonify, request
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