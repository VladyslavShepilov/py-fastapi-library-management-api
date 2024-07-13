from sqlalchemy.orm import relationship

from database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    bio = Column(String, nullable=True)
    books = relationship(
        "Book", back_populates="author",
        passive_deletes=True
    )


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    publication_date = Column(DateTime, nullable=True)
    author_id = Column(
        Integer,
        ForeignKey("authors.id", ondelete="SET NULL"),
        nullable=True
    )
    author = relationship("Author", back_populates="books")
