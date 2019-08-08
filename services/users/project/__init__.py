from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class UserAuthentication(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'authenticated'
        }


api.add_resource(UserAuthentication, '/users/authentication')
