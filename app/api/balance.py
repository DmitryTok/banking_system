from flask import Response, request
from flask_restful import Resource
from flasgger import swag_from
from app.swagger.balance import DEPOSIT_DOC, WITHDRAW_DOC

from app.service.bank import BankService


class ApiDeposit(Resource):
    route = "/deposit/"

    @swag_from(DEPOSIT_DOC)
    def post(self) -> Response:
        _bank = BankService()

        return _bank.deposit_or_withdraw(
            data=request.args.to_dict(), is_deposit=True
        )


class ApiWithdraw(Resource):
    route = "/withdraw/"

    @swag_from(WITHDRAW_DOC)
    def post(self) -> Response:

        _bank = BankService()

        return _bank.deposit_or_withdraw(
            data=request.args.to_dict(), is_deposit=False
        )
