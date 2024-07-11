from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas


def get_all_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()


def get_author(db: Session, author_id: int):
    db_author = db.query(models.Author).filter(
        models.Author.id == author_id
    ).first()
    return db_author


def create_author(db: Session, author: schemas.AuthorBase):
    author_db = models.Author(
        name=author.name,
        bio=author.bio
    )
    db.add(author_db)
    db.commit()

    db.refresh(author_db)
    return author


def update_author_model(db: Session, author: schemas.AuthorBase):
    author_db = db.query(models.Author).filter(
        models.Author.id == author.id
    ).first()
    if author_db:
        author_db.name = author.name
        author_db.bio = author.bio
        db.commit()

        db.refresh(author_db)
        return author
    return None


def delete_author(db: Session, author_id: int):
    db_author = db.query(models.Author).filter(
        models.Author.id == author_id
    ).first()
    if db_author:
        db.delete(db_author)
        db.commit()
        return True
    return False


def get_all_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_books_by_author(db: Session, author_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Book).filter(models.Book.author_id == author_id).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()
    return db_book


def create_book(db: Session, book: schemas.BookBase):
    author = get_author(db, book.author_id)
    if author is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    book_db = models.Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(book_db)
    db.commit()

    db.refresh(book_db)
    return book_db


def update_book(db: Session, book: schemas.BookBase):
    book_db = db.query(models.Book).filter(
        models.Book.id == book.id
    ).first()
    if book_db:
        book_db.name = book.title
        book_db.bio = book.summary
        book_db.publication_date = book.publication_date
        book_db.author_id = book.author_id
        db.commit()

        db.refresh(book_db)
        return book_db
    return None


def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
