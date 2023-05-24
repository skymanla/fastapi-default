from fastapi import FastAPI
from fastapi.exceptions import HTTPException, ValidationError, RequestValidationError
from app.exception import exception_handler as ex


app = FastAPI(
    title="API",
    version="0.1",
    description=""
)

# exception handler
app.add_exception_handler(HTTPException, ex.http_exception_handler)
app.add_exception_handler(RequestValidationError, ex.request_error_handler)
app.add_exception_handler(ValidationError, ex.validation_error_handler)


# routers





