from flask import Blueprint
from flask_restful import Api

from app.test.web.views import *

test = Blueprint('test', 
                        __name__,
                        static_folder='../templates/dist',
                        template_folder='../templates')

api = Api(test)
api.add_resource(ReturnEndPointData, '/<project_name>/<version>/<path:path>')
