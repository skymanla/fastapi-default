from fastapi import FastAPI
from fastapi.exceptions import HTTPException, ValidationError, RequestValidationError
from app.exception import exception_handler as ex


app = FastAPI(
    title="API",
    version="0.1",
    description="",
    responses={
        400: {
            "content": {
                "application/json": {
                    "example": {
                        "code": 400,
                        "message": "request error",
                        "data": None
                    }
                }
            }
        },
        422: {
            "content": {
                "application/json": {
                    "example": {
                        "code": 422,
                        "message": "${field}의 값이 잘못되었습니다",
                        "data": None
                    }
                }
            }
        }
    }
)

# exception handler
app.add_exception_handler(HTTPException, ex.http_exception_handler)
app.add_exception_handler(RequestValidationError, ex.request_error_handler)
app.add_exception_handler(ValidationError, ex.validation_error_handler)


# routers





