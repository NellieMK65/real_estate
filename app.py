from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db, UserModel
from resources.location import Location
from resources.property import Property
from resources.user import Signup, Login

app = Flask(__name__)
# configure db URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['BUNDLE_ERRORS'] = True
app.config['SQLALCHEMY_ECHO'] = True
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!

CORS(app)

# link migrations
migrations = Migrate(app, db)

# init our db
db.init_app(app)

# initialize flask restful
api = Api(app)

# initialize bcrypt
bcrypt = Bcrypt(app)
# initialize JWT
jwt = JWTManager(app)

# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none().to_json()

class AppResource(Resource):
    def get(self):
        return "Welcome to the real estate api"

api.add_resource(Location, '/location', '/location/<int:id>')
api.add_resource(Property, '/property', '/property/<int:id>')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
