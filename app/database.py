import logging
from itertools import count


logger = logging.getLogger(__name__)


class Database:
    def __init__(self):
        self._db = {}
        self._name_set = set()
        self._ids = count(start=1)
        logger.info("Database initialized")

    def get_next_id(self):
        next_id = next(self._ids)
        logger.info(f"Generated new account ID: {next_id}")

        return next_id

    def create_account(self, key: int, data: dict):
        self._db[key] = data
        self._name_set.add(data['name'])

        logger.info(
            f"Account created: ID={key}, Name={data['name']}, Balance={data['balance']}"
        )
        logger.info(f"Actual Name Set: {self._name_set}")

    def get_account_id(self, account_id: dict):
        account = self._db.get(account_id)

        if not account:
            logger.warning(
                f"Attempt to access non-existing account ID={account_id}"
            )
        else:
            logger.debug(f"Fetched account ID={account_id}: {account}")

        return account

    def deposit_or_withdraw(
        self, account_id: int, amount: float, is_deposit: bool
    ):
        account = self.get_account_id(account_id)

        if is_deposit:
            account["balance"] += amount
            logger.info(
                f"Deposited={amount} to account ID={account_id}, New balance={account['balance']}"
            )

        else:
            account["balance"] -= amount
            logger.info(
                f"Withdrew={amount} from account ID={account_id}, New balance={account['balance']}"
            )

    def transfer(self, from_account_id: int, to_account_id: int, amount: int):
        from_account = self.get_account_id(from_account_id)
        to_account = self.get_account_id(to_account_id)

        from_account["balance"] -= amount
        to_account["balance"] += amount

        logger.info(
            f"Transferred {amount} from account ID={from_account_id} to ID={to_account_id}. "
            f"New balances: from={from_account['balance']}, to={to_account['balance']}"
        )


db = Database()
