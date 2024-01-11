from flask import jsonify
from flask_restful import Resource
from models import LocationModel

class AppResource(Resource):
    def get(self):
        return "Welcome to the real estate api"

class LocationList(Resource):
    # will return  a list of locations
    def get(self):
        return "My first flask-restful app"

    def post(self):
        return

class Location(Resource):
    # get a single location
    def get(self, id):
        location = LocationModel.query.filter_by(id = id).first()
        print(location.json())
        # print(f"Retrieving {id}")
        return jsonify(location.json())

    def put(self, id):
        print(f"Updating {id}")
        return "Location update"

    def delete(self, id):
        print(f"Deleting #{id}")
        return


