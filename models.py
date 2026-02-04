from pydantic import BaseModel
from typing import Optional

# Base properties shared across all schemas
class BookBase(BaseModel):
    title: str
    # Making these Optional allows the API to handle the null values in your CSV
    author: str | None = "Unknown Author"
    year: int | None = 0
    isbn: str | None = None
    publisher: str | None = None
    image_url: str | None = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    isbn: str | None = None
    publisher: str | None = None
    image_url: str | None = None

class BookResponse(BookBase):
    id: int

    # This allows Pydantic to convert SQLAlchemy objects to JSON automatically
    model_config = {
        "from_attributes": True
        }

class DeleteResponse(BaseModel):
    message: str
    book: BookResponse | None = None