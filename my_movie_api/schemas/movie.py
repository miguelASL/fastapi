from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional, List, Dict

# Schema
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=50)
    overview: str = Field(min_length=1, max_length=50)
    year: int = Field(Le = 2024)
    rating: float = Field(ge = 0, le = 10)
    category: str = Field(min_length=1, max_length=50)
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi Pelicula",
                "overview": "The story spans ten years from 1945 to 1955 and chronicles the fictional Italian-American Corleone crime family.",
                "year": 2022,
                "rating": 9.2,
                "category": "drama" 
            }
        }