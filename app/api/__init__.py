from flask import Response, request
from flask_restful import Resource


class ApiListCourse(Resource):
    route = '/api/create_account/'

    def get(self) -> Response:
        pass
