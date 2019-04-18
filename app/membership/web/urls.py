from flask import Blueprint
from flask_restful import Api

from app.membership.web.views import *

membership = Blueprint('membership', __name__)
api = Api(membership)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')