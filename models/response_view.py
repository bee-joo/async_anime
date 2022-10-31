from bson import ObjectId
from models import anime, movie
from pydantic import BaseModel


class ResponseView(BaseModel):
    anime: anime.Anime
    movie: movie.Movie

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }