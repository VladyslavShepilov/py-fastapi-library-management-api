from pydantic import BaseModel
from pydantic.fields import Optional
from sqlalchemy import DateTime


class AuthorBase(BaseModel):
    id: Optional[int]
    name: str
    bio: Optional[str] = None


class BookBase(BaseModel):
    id: Optional[int]
    title: str
    summary: Optional[str] = None
    publication_date: Optional[DateTime] = None
    author_id: int
