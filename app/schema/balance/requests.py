from pydantic import BaseModel, Field


class DepositOrWithdrawRequest(BaseModel):
    account_id: int
    amount: float = Field(gt=0)
