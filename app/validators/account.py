from app.database import db


class AccountValidators:

    @staticmethod
    def validate_name(name: str) -> bool:
        return name not in db._name_set

    @staticmethod
    def validate_account_id(account_id: int) -> bool:
        return db.get_account_id(account_id) is not None

    @staticmethod
    def validate_balance(balance: int, amount: float) -> bool:
        return balance >= amount
