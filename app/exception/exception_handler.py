from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.encoders import jsonable_encoder


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "message": str(exc.detail),
            "data": None
        }
    )


async def request_error_handler(request: Request, exc: RequestValidationError):
    exc_json = jsonable_encoder(exc.errors())
    response = {"code": 422, "message": "", "data": None}
    for error in exc_json:
        # response['message'].append(error['loc'][-1]+f": {error['msg']}")
        response['message'] = error['loc'][-1] + f"의 값이 잘못되었습니다"

    return JSONResponse(response, status_code=422)


async def validation_error_handler(request: Request, exc: ValidationError):
    exc_json = exc.errors()
    response = {"code": 400, "message": "", "data": None}
    for error in exc_json:
        response['message'] = error['msg']

    return JSONResponse(response, status_code=400)
