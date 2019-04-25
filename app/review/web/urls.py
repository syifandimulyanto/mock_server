from flask import Blueprint
from flask_restful import Api

from app.review.web.views import *

review = Blueprint('review', 
                        __name__,
                        static_folder='../templates/dist',
                        template_folder='../templates/')

api = Api(review)
api.add_resource(Display, '/<project_name>')