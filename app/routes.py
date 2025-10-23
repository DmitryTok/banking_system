from flask_restful import Api

from app.api.account import ApiRegistration
from app.api.balance import ApiDeposit, ApiWithdraw
from app.api.transfer import ApiTransfer


def api_routes(api: Api):
    api.add_resource(ApiRegistration, ApiRegistration.route)
    api.add_resource(ApiDeposit, ApiDeposit.route)
    api.add_resource(ApiWithdraw, ApiWithdraw.route)
    api.add_resource(ApiTransfer, ApiTransfer.route)
