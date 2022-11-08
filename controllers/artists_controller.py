from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist
from schemas.artist_schema import artist_schema

artists = Blueprint('artists', __name__, url_prefix="/artist")


# 127.0.0.1:5000/artist
# This returns all artists/the sole artist's bio

@artists.route("/", methods=["GET"])
def artist_info():
    artist_list = Artist.query.all()
    result = artist_schema.dump(artist_list)
    return jsonify(result)

# 127.0.0.1:5000/artist
# This is an add method for creating a new artist.
# For the purpose of this exercise, this API reflects one artist's Artreon content with the associated users to that artist.

@artists.route("/", methods=["POST"])
def add_artist():
    artist_fields = artist_schema.load(request.json)

    new_artist = Artist()
    new_artist.artreon_alias = artist_fields["artreon_alias"]
    new_artist.password = artist_fields["password"]
    new_artist.email = artist_fields["email"]
    new_artist.is_admin = artist_fields["is_admin"]
    new_artist.artist_bio = artist_fields["artist_bio"]

    db.session.add(new_artist)
    db.session.commit()

    return jsonify(artist_schema.dump(new_artist))

