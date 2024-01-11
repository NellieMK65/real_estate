from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
# configure db URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# link migrations
migrations = Migrate(app, db)

# init our db
db.init_app(app)

@app.route('/')
def index():
    return "My first flask app"
