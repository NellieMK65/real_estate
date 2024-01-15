from flask_restful import Resource, reqparse, fields, marshal_with
from flask_bcrypt import check_password_hash,generate_password_hash
from models import UserModel, db

user_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'phone': fields.String,
    'email': fields.String,
    'role': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
}

response_field = {
    "message": fields.String,
    "status": fields.String,
}

response_field['user'] = {}
response_field['user']['id'] = fields.Integer

class Signup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="Firstname is required")
    parser.add_argument('last_name', required=True, help="Last name is required")
    parser.add_argument('phone', required=True, help="Phone number is required")
    parser.add_argument('email', required=True, help="Email address is required")
    parser.add_argument('password', required=True, help="Password is required")

    @marshal_with(response_field)
    def post(self):
        data = Signup.parser.parse_args()

        # encrypt password
        data['password'] = generate_password_hash(data['password'])
        # set default role
        data['role'] = 'member'

        user = UserModel(**data)

        # verify email and phone uniqueness before saving to the db
        email = UserModel.query.filter_by(email = data['email']).one_or_none()

        if email:
            return {"message": "Email already taken", "status": "fail"}, 400

        phone = UserModel.query.filter_by(phone = data['phone']).one_or_none()

        if phone:
            return {"message": "Phone number already exists", "status": "fail"}, 400

        try:
            # save user to db
            db.session.add(user)
            db.session.commit()
            # get user from db after saving
            db.session.refresh(user)

            return {"message": "Account created successfully", "status": "success", "user": user }
        except:
            return {"message": "Unable to create account", "status": "fail"}
