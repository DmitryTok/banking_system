from flask import Response, request

from flask_restful import Resource
from flasgger import swag_from
from app.swagger.account import CREATE_ACCOUNT_DOC

from app.service.bank import BankService


class ApiRegistration(Resource):
    route = "/create_account/"

    @swag_from(CREATE_ACCOUNT_DOC)
    def post(self) -> Response:
        _bank = BankService()

        return _bank.create_account(data=request.get_json())
