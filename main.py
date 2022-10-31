from fastapi import FastAPI, Depends
from routers import movie
import uvicorn

app = FastAPI()
app.include_router(movie.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)