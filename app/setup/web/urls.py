from flask import Blueprint
from flask_restful import Api

from app.setup.web.views import *

setup = Blueprint('setup', 
                        __name__,
                        static_folder='../templates/dist',
                        template_folder='../templates')

api = Api(setup)
api.add_resource(ProjectRevision, '/revision/<project_name>/<version>')
api.add_resource(ProjectSchema, '/schema/<project_name>/<version>')
