from pydantic import BaseModel
from pydantic.fields import Optional
from datetime import datetime


class AuthorBase(BaseModel):
    id: Optional[int]
    name: str
    bio: Optional[str]

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    id: Optional[int]
    title: str
    summary: Optional[str]
    publication_date: Optional[datetime]
    author_id: Optional[int]

    class Config:
        orm_mode = True
