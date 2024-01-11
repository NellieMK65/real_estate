from flask_sqlalchemy import SQLAlchemy

# initialize db
db = SQLAlchemy()

# models
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    role = db.Column(db.Text, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=db.func.now())
    # isDeleted = db.Column(db.Boolean, server_default=False)
    # deleted_at = db.Column(db.TIMESTAMP)

    # WHERE deleted_at IS NULL

class LocationModel(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=db.func.now())

    def json(self):
        return {'id': self.id, 'name': self.name, 'created_at': self.created_at,
                'updated_at': self.updated_at}

class PropertyModel(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.String, nullable=False)
    listing_price = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    type_of_property = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=db.func.now())

