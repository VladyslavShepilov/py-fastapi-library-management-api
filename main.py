from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import crud

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/authors/", response_model=list[schemas.AuthorBase])
def get_authors(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    return crud.get_all_authors(db, skip=skip, limit=limit)


@app.post("/authors/", response_model=schemas.AuthorBase)
def create_author(
    author: schemas.AuthorBase,
    db: Session = Depends(get_db),
):
    new_author = crud.create_author(db=db, author=author)
    return new_author


@app.get("/authors/{author_id}/", response_model=schemas.AuthorBase)
def get_author_by_id(
        author_id: int,
        db: Session = Depends(get_db)
):
    author = crud.get_author(db=db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.get("/books/", response_model=list[schemas.BookBase])
def get_books(
    author_id: int = None,
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    if author_id is not None:
        books = crud.get_books_by_author(db, author_id, skip=skip, limit=limit)
    else:
        books = crud.get_all_books(db, skip=skip, limit=limit)
    return books


@app.get("/books/{book_id}/", response_model=schemas.BookBase)
def get_book_by_id(
        book_id: int,
        db: Session = Depends(get_db)
):
    book = crud.get_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books/", response_model=schemas.BookBase)
def create_book(
        book: schemas.BookBase,
        db: Session = Depends(get_db)
):
    new_book = crud.create_book(db=db, book=book)
    return new_book
