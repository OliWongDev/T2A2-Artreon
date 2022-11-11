from flask import Blueprint, jsonify, request
from main import db, bcrypt
from models.artists import Artist, ArtistSchema
from controllers.auth_controller import authorize_artist
from flask_jwt_extended import jwt_required, get_jwt_identity

artists = Blueprint('artists', __name__, url_prefix="/artists")


# 127.0.0.1:5000/artists
# This returns the first artist's information AKA the sole creator/admin of the API.

@artists.route("/", methods=["GET"])
def artist_info():
    artist_list = db.select(Artist).order_by(Artist.id.asc())
    result = db.session.scalar(artist_list)
    return ArtistSchema(exclude=["password"]).dump(result), 200


# 127.0.0.1:5000/artists
# This is an add method for creating a new artist. This is only authorized for an artist themselves to do.
# For the purpose of this exercise, this API reflects one artist's Artreon content with the associated users to that artist. It is unlikely this route would be needed.

@artists.route("/", methods=["POST"])
@jwt_required()
def add_artist():
    authorize_artist()
    new_artist_fields = ArtistSchema().load(request.json)
    new_artist = Artist(
        artreon_alias = new_artist_fields["artreon_alias"],
        password = bcrypt.generate_password_hash(new_artist_fields["password"]).decode("utf-8"),
        email = new_artist_fields["email"],
        is_admin = new_artist_fields["is_admin"],
        artist_bio = new_artist_fields["artist_bio"])
    

    db.session.add(new_artist)
    db.session.commit()
    return ArtistSchema().dump(new_artist), 201

