from fastapi import APIRouter
from app.models.Movie import Movie


router = APIRouter()

@router.post("/movies")
def add_movie(movie:Movie):
    movie_dict = movie.model_dump()
    
    return {
        "message": "Movie added successfully",
        "movie" : movie_dict
    }