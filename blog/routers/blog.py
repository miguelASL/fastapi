from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)

get_db = database.get_db

@router.get("/", status_code=200, response_model=List[schemas.ShowBlog], current_user: schemas.User = Depends(oauth2.get_current_user))
def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED, current_user: schemas.User = Depends(oauth2.get_current_user)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, current_user: schemas.User = Depends(oauth2.get_current_user)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, current_user: schemas.User = Depends(oauth2.get_current_user)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.get("/{id}", status_code=200, response_model=list[schemas.ShowBlog], current_user: schemas.User = Depends(oauth2.get_current_user)
def show(id, response: Response, db: Session = Depends(get_db)):
    return blog.show(id, db)
    