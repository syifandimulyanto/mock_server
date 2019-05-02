from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from pydantic import ValidationError

from app.test.models import DataFromUser

class ReturnEndPointData(Resource):

    # def __init__(self, project_name, version, path):

    #     data_from_user = {
    #         'project_name': project_name,
    #         'version': version,
    #         'path': path,
    #         'method': method
    #     }

    #     requested_data = DataFromUser(data_from_user)


    # Retrieve data will be called via factory
    # move to bridge.service 

    def retrieve_data(self, project_name, version, path, method) -> dict:
        '''
            Retrieve data from db from specific request
        '''

        data = {
            'project_name': project_name,
            'version': version,
            'path': path,
            'method': method
        }

        return data

    # End of retrieve data

    
    def respond_data(self, data):
        '''
            Formatting data as a json
        '''
        headers = {'Content-Type': 'application/json'}
        return_code = 200

        return make_response(
            jsonify(data)
            , return_code, headers)

    def get(self, project_name, version, path):
        data = self.retrieve_data(project_name, version, path, request.method)
        return self.respond_data(data)

    def post(self, project_name, version, path):
        data = self.retrieve_data(project_name, version, path, request.method)
        return self.respond_data(data)

    def put(self, project_name, version, path):
        data = self.retrieve_data(project_name, version, path, request.method)
        return self.respond_data(data)

    def update(self, project_name, version, path):
        data = self.retrieve_data(project_name, version, path, request.method)
        return self.respond_data(data)

    def delete(self, project_name, version, path):
        data = self.retrieve_data(project_name, version, path, request.method)
        return self.respond_data(data)