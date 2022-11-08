from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist
from schemas.artist_schema import ArtistSchema

artists = Blueprint('artists', __name__, url_prefix="/artists")


# 127.0.0.1:5000/artists
# This returns all artists/the sole artist's bio

@artists.route("/", methods=["GET"])
def artist_info():
    artist_list = db.select(Artist).order_by(Artist.id.desc())
    result = db.session.scalars(artist_list)
    return ArtistSchema().dump(result)

# 127.0.0.1:5000/artists
# This is an add method for creating a new artist.
# For the purpose of this exercise, this API reflects one artist's Artreon content with the associated users to that artist.

@artists.route("/", methods=["POST"])
def add_artist():
    new_artist_fields = ArtistSchema().load(request.json)
    new_artist = Artist(
        artreon_alias = new_artist_fields["artreon_alias"],
        password = new_artist_fields["password"],
        email = new_artist_fields["email"],
        is_admin = new_artist_fields["is_admin"],
        artist_bio = new_artist_fields["artist_bio"])
    

    db.session.add(new_artist)
    db.session.commit()
    return ArtistSchema().dump(new_artist), 201

