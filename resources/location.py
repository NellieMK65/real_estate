from flask_restful import Resource, fields, marshal_with, reqparse
from models import LocationModel, db

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
}

class Location(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help="Location name is required")

    # get a single location
    @marshal_with(resource_fields)
    def get(self, id=None):
        # if the id is present we get a single location
        # else we get all locations
        if id:
            location = LocationModel.query.filter_by(id = id).first()

            return location
        else:
            locations = LocationModel.query.all();

            return locations

    def post(self):
        data = Location.parser.parse_args()
        # unpacks a dict add passes it as key-value pairs
        # {"title": "Ngong"} -> title: "Ngong"
        location = LocationModel(**data)

        try:
            db.session.add(location)
            db.session.commit()

            return {"message": "Location created successfully"}
        except:
            return {"message": "Unable to save location"}

