from enum import Enum
from pydantic import BaseModel, EmailStr, Field, ConfigDict, NaiveDatetime


class TicketStatus(str, Enum):
    OPEN = "OPEN"
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"


class TicketCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100)
    customer_email: EmailStr
    subject: str = Field(min_length=1, max_length=255)
    message: str = Field(min_length=1)

class TicketResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: EmailStr
    subject: str
    message: str
    status: TicketStatus
    created_at: NaiveDatetime
    updated_at: NaiveDatetime

    model_config = ConfigDict(from_attributes=True)