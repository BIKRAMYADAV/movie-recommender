from fastapi import FastAPI
from app.routes.Movies import router as movie_router

app = FastAPI(title="movie recommender")

app.include_router(movie_router)