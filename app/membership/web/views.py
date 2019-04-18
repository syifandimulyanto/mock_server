from flask import request
from flask_restful import Resource
from pydantic import ValidationError

from app.membership.models import Member

class Register(Resource):
    def post(self):
        try:
            new_member = Member(**request.json)
        except ValidationError as e:
            '''
            If model is not suitable
            '''
            return {"code": 400, "error_found": e.errors()}, 400

        return {"code": 200, "msg": "success"}, 200
        
class Login(Resource):
    def post(self):
        try:
            new_member = Member(**request.json)
        except ValidationError as e:
            '''
            If model is not suitable
            '''
            return {"code": 400, "error_found": e.errors()}, 400

        return {"code": 200, "msg": "success"}, 200