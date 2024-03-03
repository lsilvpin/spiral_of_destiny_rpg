import sys, os

from main.libraries.di_container import Container

sys.path.insert(0, os.path.abspath("."))
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exceptions import HTTPException

container = Container()
app = FastAPI()
app.container = container

# Controllers
from main.apps.microservice.controllers.character_controller import (
    router as character_router,
)

# Routes
app.include_router(character_router)


# Exception Handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400, content={"message": "Validation Error", "detail": exc.errors()}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
