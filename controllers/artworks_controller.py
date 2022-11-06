from flask import Blueprint, jsonify, request
from main import db
from models.artworks import Artwork
from schemas.artwork_schema import artwork_schema, artworks_schema

artworks = Blueprint('artworks', __name__, url_prefix="/artworks")

# 127.0.0.1:5000/artworks
# This returns the artworks

@artworks.route("/", methods = ["GET"])
def get_all_artworks():
     artworks_list = Artwork.query.all()
     result = artworks_schema.dump(artworks_list)
     return jsonify(result)

# 127.0.0.1:5000/artworks/<int:id>
# This returns a single artwork 

@artworks.route("/<int:id>", methods=["GET"])
def get_single_artwork(id):
    artwork = Artwork.query.filter_by(id=id).first()
    # if not artwork_comment:
    #     return abort
    result = artwork_schema.dump(artwork)
    return jsonify(result)
