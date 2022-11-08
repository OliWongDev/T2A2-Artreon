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
    # 1. Take the artist_schema because it is us templating it through Marshmallow to prepare for the process of updating the artist's details.
    # 2. Start with the request.json --> We are requesting the JSON object in the DB (artist's details) and parsing it into a Javascript object.
    # 3. Load --> We are deserializing this javascript object so that it can be changed within the route function. It's 
    # Notice with the below lines, I'm able to access the items in a list that started from our schema template to set their updated values.
    new_artist = Artist()
    new_artist.artreon_alias = artist_fields["artreon_alias"]
    new_artist.password = artist_fields["password"]
    new_artist.email = artist_fields["email"]
    new_artist.is_admin = artist_fields["is_admin"]
    new_artist.artist_bio = artist_fields["artist_bio"]

    db.session.add(new_artist)
    db.session.commit()
    # 1. Reversing the process, our python object 'new_artist' has some updated values. Let's send it back.
    # 2. Dump serializes the new_artist object back to a Javascript object.
    # 3. Jsonify serializes all the arguments in the brackets to JSON. Can't go from 1 to 3.
    return jsonify(artist_schema.dump(new_artist))

