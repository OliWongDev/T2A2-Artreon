from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist
from schemas.artist_schema import artist_schema

artists = Blueprint('artists', __name__, url_prefix="/artist")


# 127.0.0.1:5000/artist
# This returns the artist's bio

@artists.route("/", methods=["GET"])
def artist_info():
    artist_list = Artist.query.all()
    result = artist_schema.dump(artist_list)
    return jsonify(result)