from fastapi import FastAPI, Body, Path, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Coroutine, Optional, List, Dict
from starlette.requests import Request
from util.jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config.database import Session, engine, Base
from router.movie import movie_router, user_router

app = FastAPI(title="My Movie API", description="This is a very fancy movie API.", version="0.0.1")
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Coroutine[Any, Any, HTTPAuthorizationCredentials or None]:
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=401, detail="Unauthorized")

movies = [
    {
        "id": 1,
        "title": "The Godfather",
        "overview": "The story spans ten years from 1945 to 1955 and chronicles the fictional Italian-American Corleone crime family.",
        "year": 1972,
        "rating": 9.2,
        "category": "drama" 
    },
       {
        "id": 2,
        "title": "Naruto",
        "overview": "This new story tells of House Forrester, a noble family from the north of Westeros, loyal to the Starks of Winterfell.",
        "year": 1995,
        "rating": 9.1,
        "category": "Funny" 
    }
]

@app.get("/", tags=["home"])
def message():
    return HTMLResponse(content="<h1>Welcome to my movie API</h1>", status_code=200)


        