from fastapi import FastAPI, Body, Path, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from util.jwt_manager import create_token, validate_token
from schemas.user import User

user_router = FastAPI()
    
@user_router.post("/login", tags=["auth"], response_model=dict, status_code=200)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "12345678":
        token : str = create_token(data=user.dict())
        return JSONResponse(content={"message": "Login successful"}, status_code=200)
    return JSONResponse(content={"message": "Incorrect email or password"}, status_code=401)

