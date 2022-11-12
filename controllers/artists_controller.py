from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt
from models.artists import Artist, ArtistSchema
from controllers.auth_controller import authorize_artist, authorize_user, authorize_paid_user
from flask_jwt_extended import jwt_required, get_jwt_identity



artists = Blueprint('artists', __name__, url_prefix="/artists")


# 127.0.0.1:5000/artists
# This returns all Artists on the Graphic God Artreon.

@artists.route("/", methods=["GET"])
@jwt_required()
def get_all_artists():
    artist_list = db.select(Artist).order_by(Artist.id.asc())
    result = db.session.scalars(artist_list)
    return ArtistSchema(many=True, exclude=["password"]).dump(result)


# 127.0.0.1:5000/artists/<int:id>
# This returns a single artist's information and their content.

@artists.route("/<int:id>", methods=["GET"])
def get_one_artist(id):
    artist = db.select(Artist).filter_by(id=id)
    result = db.session.scalar(artist)
    return ArtistSchema(exclude=["password"]).dump(result), 200


# 127.0.0.1:5000/artists/<str:artreon_alias>
# This allows you to grab an artist by their alias

@artists.route("/<string:artreon_alias>", methods=["GET"])
def get_artist_by_alias(artreon_alias):
    artist = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    result = db.session.scalar(artist)
    return ArtistSchema(exclude=["password"]).dump(result), 200


@artists.route("/<string:artreon_alias>", methods=["PUT", "PATCH"])
def update_artist_details(artreon_alias):
    artist_data = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    artist = db.session.scalar(artist_data)
    if artist:
        artist.artreon_alias = request.json.get("artreon_alias") or artist.artreon_alias
        artist.password = request.json.get("password") or artist.password
        artist.email = request.json.get("email") or artist.email
        artist.artist_bio = request.json.get("artist_bio") or artist.artist_bio
        return ArtistSchema().dump(artist)
    else:
        return abort(404, description="The artist does not exist")


@artists.route("/<string:artreon_alias>", methods=["DELETE"])
def delete_artist_account(artreon_alias):
    artist_statement = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    artist = db.session.scalar(artist_statement)
    if artist:
        db.session.delete(artist)
        db.session.commit()
        return {'message': f"The user '{artreon_alias}' was deleted successfully"}
    else:
        return {"error": f"The artist with the name {artreon_alias} was not found to be deleted."}, 404


@artists.route("/<string:artreon_alias>/artworks", methods=["GET"])
def get_all_artist_artworks(artreon_alias):
    artist_statement = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    artist = db.session.scalar(artist_statement)
    return ArtistSchema(only=("artreon_alias", "artworks")).dump(artist), 200

@artists.route("/<string:artreon_alias>/walkthroughs", methods=["GET"])
def get_all_artist_walkthroughs(artreon_alias):
    artist_statement = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    artist = db.session.scalar(artist_statement)
    return ArtistSchema(only=["artreon_alias", "walkthroughs"]).dump(artist), 200

@artists.route("/<string:artreon_alias>/emails", methods=["GET"])
def get_all_artist_emails(artreon_alias):
    artist_statement = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    artist = db.session.scalar(artist_statement)
    return ArtistSchema(only=["artreon_alias", "emails"]).dump(artist), 200

@artists.route("/<string:artreon_alias>/walkthroughs", methods=["GET"])
def get_all_artist_q_and_as(artreon_alias):
    artist_statement = db.select(Artist).filter_by(artreon_alias=artreon_alias)
    artist = db.session.scalar(artist_statement)
    return ArtistSchema(only=["artreon_alias", "q_and_as"]).dump(artist), 200

