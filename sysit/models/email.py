from freenit.models.base import ModelsBase
from pydantic import BaseModel


class EmailBase(BaseModel):
    email: str
    subject: str
    message: str


class EmailListing(EmailBase):
    pass


class EmailResponse(EmailBase):
    pass


models = ModelsBase(EmailBase, EmailListing, EmailResponse)
