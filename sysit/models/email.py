from pydantic import BaseModel


class Email(BaseModel):
    email: str
    subject: str
    message: str
