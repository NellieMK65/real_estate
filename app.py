from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from resources import Location, AppResource

app = Flask(__name__)
# configure db URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# link migrations
migrations = Migrate(app, db)

# init our db
db.init_app(app)

# initialize flask restful
api = Api(app)

api.add_resource(AppResource, '/')

api.add_resource(Location, '/location/<int:id>')

