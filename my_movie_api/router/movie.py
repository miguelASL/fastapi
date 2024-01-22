from fastapi import APIRouter
from fastapi import FastAPI, Body, Path, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Coroutine, Optional, List, Dict
from config.database import Session, engine, Base
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200, dependencies = [Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie()
    return JSONResponse(content = jsonable_encoder(result), status_code=200)

@movie_router.get("/movies/{movie_id}", tags=["movies"], response_model=Movie, status_code=200)
def get_movie(movie_id: int) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(movie_id)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movie_category(category: str = Query(min_length=5, max_length=20)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.post("/movies", tags=["movies"], response_model = dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado la pelicula"}, status_code=200)

@movie_router.put("/movies/{movie_id}", tags=["movies"], response_model = dict, status_code=200)
def update_movie(id : int, movie: Movie) -> dict:
    db = Session()
    movie = MovieService(db).update_movie(id, movie)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    MovieService(db).update_movie(id, movie)
    db.commit()
    return JSONResponse(content={"message": "Se ha actualizado la pelicula"}, status_code=200)

@movie_router.delete("/movies/{movie_id}", tags=["movies"], response_model = dict, status_code=200)
def delete_movie(movie_id: int):
    db = Session()
    movie = MovieService(db).delete_movie(movie_id)
    if not movie:
       raise HTTPException(status_code=404, detail="Movie not found")
    MovieService(db).delete_movie(movie_id)
    return JSONResponse(content={"message": "Se ha eliminado la pelicula"}, status_code=200)