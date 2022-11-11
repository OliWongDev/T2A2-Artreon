from flask import Blueprint, request, abort
from main import db, bcrypt
from datetime import timedelta
from models.users import User, UserSchema
from models.artists import Artist, ArtistSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/users')
def get_users():
    user_select = db.select(User)
    users = db.session.scalars(user_select)
    return UserSchema(many=True, exclude=['password']).dump(users)

@auth.route('/register', methods=['POST'])
def auth_register_user():
    try:
        user = User(
            user_alias = request.json['email'],
            first_name = request.json.get('first_name'),
            last_name = request.json.get('last_name'),
            join_date = request.json['join_date'],
            email = request.json['email'],
            has_subscription = request.json['has_subscription'],
            password = bcrypt.generate_password_hash(request.json['password'].decode('utf-8'))
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


@auth.route('/login', methods=['POST'])
def auth_login():
    user_statement = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(user_statement)

    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=12))
        return {'email': user.email, 'token': token}
    else:
        return {'error': 'The email or password was invalid'}, 401


def authorize_paid_user():
    user_id = get_jwt_identity()
    user_statement = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(user_statement)

    if not user.has_subscription:
        return {'error': 'Sorry, as a free user you are not authorized to view this content.'}, 401

def authorize_user():
    user_id = get_jwt_identity()
    user_statement = db.Select(User).filter_by(id=user_id)
    return user_statement

def authorize_precise_user(id):
    user_id = get_jwt_identity()
    user_statement = db.Select(User).filter_by(id=user_id)
    user = db.session.scalar(user_statement)
    if user.id !=id:
        abort(401)


@auth.route('/artist_login', methods=['POST'])
def auth_artist_login():
    artist_statement = db.select(Artist).filter_by(email=request.json['email'])
    artist = db.session.scalar(artist_statement)

    if artist and bcrypt.check_password_hash(artist.password, request.json['password']):

        token = create_access_token(identity=str(artist.id), expires_delta=timedelta(hours=12))
        return {'email': artist.email, 'token': token}
    else:
        return {'error': 'The email or password was invalid'}, 401


def authorize_artist():
    artist_id = get_jwt_identity()
    artist_statement = db.select(Artist).filter_by(id=artist_id)
    artist = db.session.scalar(artist_statement)
    if not artist.is_admin:
        return abort(401), False


def authorize_general_artist():
    artist_id = get_jwt_identity()
    artist_statement = db.select(Artist).filter_by(id=artist_id)
    return artist_statement

def authorize_precise_artist(id):
    artist_id = get_jwt_identity()
    artist_statement = db.Select(Artist).filter_by(id=artist_id)
    artist = db.session.scalar(artist_statement)
    if artist.id != id:
        abort(401)
