from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# set config
app.config.from_object('project.config.DevelopmentConfig')


class UserAuthentication(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'authenticated'
        }


api.add_resource(UserAuthentication, '/users/authentication')
