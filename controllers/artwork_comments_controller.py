from flask import Blueprint, jsonify, request
from main import db
from models.artwork_comments import ArtworkComment

artwork_comments = Blueprint('artwork_comments', __name__, url_prefix="/artwork_comments")