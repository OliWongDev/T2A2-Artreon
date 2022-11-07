from flask import Blueprint, jsonify, request, abort
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
    # if not artwork:
    #     return abort
    result = artwork_schema.dump(artwork)
    return jsonify(result)

#127.0.0.1:5000/artworks
#### This allows the artist to CREATE and post an artwork

@artworks.route("/", methods=["POST"])
def add_artwork():

     artwork_fields = artwork_schema.load(request.json)

     new_artwork = Artwork()
     new_artwork.artwork_name = artwork_fields["artwork_name"]
     new_artwork.description = artwork_fields["description"]
     new_artwork.date = artwork_fields["date"]
     new_artwork.artist_id = artwork_fields["artist_id"]

     db.session.add()
     db.session.commit()

     return jsonify(artwork_schema.dump(new_artwork))

@artworks.route("/<int:id>", methods=["DELETE"])
def delete_artwork(id):

     artwork = Artwork.query.filter_by(id=id).first()
     if not artwork:
          return abort(400, description="This artwork does not exist to be deleted.")
     
     db.session.delete()
     db.session.commit()

     return jsonify(artwork_schema.dump(artwork))


