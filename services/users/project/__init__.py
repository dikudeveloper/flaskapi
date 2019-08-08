import os

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


class UserAuthentication(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'authenticated'
        }


api.add_resource(UserAuthentication, '/users/authentication')
