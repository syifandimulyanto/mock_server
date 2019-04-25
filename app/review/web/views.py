from flask import render_template
from flask_restful import Resource
from pydantic import ValidationError

# from app.review.models import Member

class Display(Resource):
    def get(self, project_name):
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

        fields = {
            'app_name': app_name,
            'config_json': default_config
        }

        

        return render_template('index.template.html', **fields)