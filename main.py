from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.routes import router
from settings import PORT, DEV, HOST

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def docs():
    return RedirectResponse(url="/docs")


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT or 8000, log_level="info", reload=DEV)
