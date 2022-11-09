from flask import Blueprint, jsonify, request, abort
from main import db
from models.artworks import Artwork
from schemas.artwork_schema import ArtworkSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorize_general_artist

artworks = Blueprint('artworks', __name__, url_prefix="/artworks")

# 127.0.0.1:5000/artworks
# This returns the artworks

@artworks.route("/", methods = ["GET"])
def get_all_artworks():
     artworks_list = db.select(Artwork).order_by(Artwork.id.asc())
     result = db.session.scalars(artworks_list)
     return ArtworkSchema(many=True).dump(result), 200

# 127.0.0.1:5000/artworks/<int:id>
# This returns a single artwork 

@artworks.route("/<int:id>", methods=["GET"])
def get_single_artwork(id):
    artwork = db.select(Artwork).filter_by(id=id)
    # if not artwork:
    #     return abort
    result = db.session.scalar(artwork)
    return ArtworkSchema().dump(result), 200

#127.0.0.1:5000/artworks
#### This allows the artist to CREATE and post an artwork
# Get JWT IDENTITY ADD
@artworks.route("/", methods=["POST"])
@jwt_required()
def add_artwork():
     authorize_general_artist()
     artwork_fields = ArtworkSchema().load(request.json)

     new_artwork = Artwork(
          artwork_name = artwork_fields["artwork_name"],
          description = artwork_fields["description"],
          date = artwork_fields["date"],
          artist_id = artwork_fields["artist_id"] 
     )

     db.session.add(new_artwork)
     db.session.commit()

     return jsonify(ArtworkSchema().dump(new_artwork))


# 127.0.0.1:5000/artworks/<int:id>
#### This allows the artist to DELETE an artwork
# JWT required
@artworks.route("/<int:id>", methods=["DELETE"])
def delete_artwork(id):

     artwork_delete_statement = db.select(Artwork).filter_by(id=id)
     artwork = db.session.scalar(artwork_delete_statement)
     if artwork:
          db.session.delete(artwork)
          db.session.commit()
     else: 
          return abort(404, description="The artwork to be deleted was not found")



