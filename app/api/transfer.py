from flask import Response, request
from flask_restful import Resource
from flasgger import swag_from
from app.swagger.transfer import TRANSFER_DOC

from app.service.bank import BankService


class ApiTransfer(Resource):
    route = "/transfer/"

    @swag_from(TRANSFER_DOC)
    def post(self) -> Response:

        _bank = BankService()

        return _bank.transfer(data=request.args.to_dict())
