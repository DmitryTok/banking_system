from pydantic import BaseModel
from app.schema.account.responses import AccountResponse


class TransferResponse(BaseModel):
    from_account: AccountResponse
    to_account: AccountResponse
