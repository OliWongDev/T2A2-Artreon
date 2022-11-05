from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist

artists = Blueprint('artists', __name__, url_prefix="/artist")


# 127.0.0.1:5000/artist
# This returns the artist's bio

@artists.route("/", methods=["GET"])
def artist_info():
    return "Welcome to the Artist's Bio!"