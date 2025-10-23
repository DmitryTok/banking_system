from http import HTTPStatus


class BankErrorHandler:

    def __init__(self):
        self.error = "error"

    def handle_name_exists_error(self, name: str):
        return {
            self.error: f"Account with {name} already exists"
        }, HTTPStatus.BAD_REQUEST

    def handle_account_not_found_error(self):
        return {self.error: f"Not Found"}, HTTPStatus.NOT_FOUND

    def handle_balance_amount_error(self, amount: int):
        return {
            self.error: f"Actual balance less then {amount}"
        }, HTTPStatus.BAD_REQUEST
