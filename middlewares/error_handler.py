from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import FastAPI, Request, Response, JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__ (self, app : FastAPI) -> None:
        super().__init__(app)
        
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response or JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"message": str("Internal Server Error")}
            )