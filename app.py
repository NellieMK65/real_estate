from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db
from resources.location import Location

app = Flask(__name__)
# configure db URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# link migrations
migrations = Migrate(app, db)

# init our db
db.init_app(app)

# initialize flask restful
api = Api(app)

class AppResource(Resource):
    def get(self):
        return "Welcome to the real estate api"

api.add_resource(Location, '/location', '/location/<int:id>')

