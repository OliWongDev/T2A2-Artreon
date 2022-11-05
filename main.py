from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating our database object! This allows us to use our ORM


def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    db = SQLAlchemy(app)
    # configuring our app:
    app.config.from_object("config.app_config")

    # creating our database object! This allows us to use our ORM
    @app.route('/')
    def home():
        return 'Hello World'

    return app