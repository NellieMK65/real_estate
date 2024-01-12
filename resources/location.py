from flask_restful import Resource
from models import LocationModel

class Location(Resource):
    # get a single location
    def get(self, id):
        location = LocationModel.query.filter_by(id = id).first()
        print(location.json())
        # print(f"Retrieving {id}")
        return "single location"

    def put(self, id):
        print(f"Updating {id}")
        return "Location update"

    def delete(self, id):
        print(f"Deleting #{id}")
        return
