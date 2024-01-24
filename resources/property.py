from flask_restful import Resource, fields, marshal_with, reqparse
from flask_jwt_extended import jwt_required, current_user
from models import PropertyModel, db
from .location import resource_fields as location_fields

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'listing_price': fields.Integer,
    'type_of_property': fields.String,
    'location': fields.Nested(location_fields),
    'is_active': fields.Boolean,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
}

class Property(Resource):
    # create a new instance of reqparser
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help="Name is required")
    parser.add_argument('description', required=True, help="Description is required")
    parser.add_argument('listing_price', type=int, required=True, help="Listing price is required")
    parser.add_argument('location_id', required=True, help="Location is required")
    parser.add_argument('type_of_property', required=True, help="Type of property is required")


    @marshal_with(resource_fields)
    @jwt_required()
    def get(self, id=None):
        if id:
            property = PropertyModel.query.filter_by(id=id).first()

            return property
        else:
            properties = PropertyModel.query.all()

            return properties

    @jwt_required()
    def post(self):
        # check if user is admin
        if current_user['role'] != 'admin':
            return {"message": "Unauthorized request", "status": "fail"}, 403

        data = Property.parser.parse_args()

        property = PropertyModel(**data)

        try:
            db.session.add(property)
            db.session.commit()

            return {"message": "Property created successfully", "status": "success"}
        except:
            return {"message": "Unable to create property", "status": "fail" }



