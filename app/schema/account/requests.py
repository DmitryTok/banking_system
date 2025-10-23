from pydantic import BaseModel, Field


class AccountCreateRequest(BaseModel):
    name: str
    initial_balance: float = Field(ge=0)
