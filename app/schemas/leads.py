from pydantic import BaseModel


class BaseLead(BaseModel):
    phone_work: str
    first_name: str
    last_name: str


class LeadOut(BaseLead):
    id: int

    class Config:
        orm_mode = True
