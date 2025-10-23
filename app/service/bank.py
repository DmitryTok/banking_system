from app.database import db
from pydantic import ValidationError
from app.errorhandlers.bank import BankErrorHandler
from app.schema.account.requests import AccountCreateRequest
from app.schema.account.responses import AccountResponse
from app.schema.balance.requests import DepositOrWithdrawRequest
from app.schema.trasfer.requests import TransferRequest
from app.schema.trasfer.responses import TransferResponse
from app.validators.account import AccountValidators
from http import HTTPStatus


class BankService:
    validator = AccountValidators()
    error_handler = BankErrorHandler()

    def create_account(self, data: dict) -> AccountResponse:
        try:
            account_data = AccountCreateRequest(**data)
        except ValidationError as exc:
            return {"error": exc.errors()}, HTTPStatus.UNPROCESSABLE_ENTITY

        if not self.validator.validate_name(account_data.name):
            return self.error_handler.handle_name_exists_error(
                account_data.name
            )

        account = AccountResponse(
            id=db.get_next_id(),
            name=account_data.name,
            balance=float(account_data.initial_balance),
        )

        db.create_account(account.id, account.model_dump())

        return account.model_dump(), HTTPStatus.CREATED

    def deposit_or_withdraw(
        self,
        data: dict,
        is_deposit: bool,
    ) -> AccountResponse:
        try:
            _data = DepositOrWithdrawRequest(**data)
        except ValidationError as exc:
            return {"error": exc.errors()}, HTTPStatus.UNPROCESSABLE_ENTITY

        if not self.validator.validate_account_id(_data.account_id):
            return self.error_handler.handle_account_not_found_error()

        account = db.get_account_id(_data.account_id)

        if is_deposit:
            db.deposit_or_withdraw(
                account_id=account["id"],
                amount=float(_data.amount),
                is_deposit=is_deposit,
            )

        else:
            if not self.validator.validate_balance(
                account["balance"], float(_data.amount)
            ):
                return self.error_handler.handle_balance_amount_error(
                    _data.amount
                )

            db.deposit_or_withdraw(
                account_id=account["id"],
                amount=float(_data.amount),
                is_deposit=is_deposit,
            )

        account = AccountResponse(**account)

        return account.model_dump(), HTTPStatus.OK

    def transfer(self, data: dict) -> TransferResponse:
        try:
            _data = TransferRequest(**data)
        except ValidationError as exc:
            return {"error": exc.errors()}, HTTPStatus.UNPROCESSABLE_ENTITY

        if not self.validator.validate_account_id(
            _data.from_account_id
        ) and not self.validator.validate_account_id(_data.to_account_id):
            return self.error_handler.handle_account_not_found_error()

        from_account = db.get_account_id(_data.from_account_id)
        to_account = db.get_account_id(_data.to_account_id)

        if not self.validator.validate_balance(
            from_account["balance"], float(_data.amount)
        ):
            return self.error_handler.handle_balance_amount_error(_data.amount)

        db.transfer(
            from_account_id=from_account["id"],
            to_account_id=to_account["id"],
            amount=float(_data.amount),
        )

        response = TransferResponse(
            from_account=AccountResponse(**from_account),
            to_account=AccountResponse(**to_account),
        )

        return response.model_dump(), HTTPStatus.OK
