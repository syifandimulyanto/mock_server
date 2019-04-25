from flask import render_template, make_response
from flask_restful import Resource
from pydantic import ValidationError

class DisplaySwaggerUI(Resource):
    def get(self, project_name):
        '''
            Processing Mock API to swagger UI
        '''
        
        # Getting App name, api uri and all config
        # Later, we will use factory or gateway to receive it

        if project_name == 'tegar':
            app_name = "Tegar File"
            api_url = 'http://petstore.swagger.io/v2/swagger.json'
        else:
            app_name = "Not Tegar File"
            api_url = 'file:///Users/tegarimansyah/alterra/mock_api_server/app/review/archive/json_example.json'
        
        default_config = {
            'dom_id': '#swagger-ui',
            'url': api_url,
            'layout': 'StandaloneLayout'
        }

        all_config = {
            'app_name': app_name,
            'config_json': default_config
        }

        # End of Getting App name, api uri and all config

        headers = {'Content-Type': 'text/html'}

        return make_response(
            render_template('index.template.html', **all_config)
            , 200, headers)