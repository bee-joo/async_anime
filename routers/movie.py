from db.operations import OpsForMongo
from fastapi import APIRouter, Depends, HTTPException, Query
from models.movie import Movie
from models.response_view import ResponseView
import aiohttp
import db.mongo as db

router = APIRouter()


@router.get("/{id}", response_model=ResponseView)
async def get_anime(id: int, ops: OpsForMongo = Depends(db.get_movie_ops)):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.jikan.moe/v4/anime/{id}") as resp:
            if resp.status != 200:
                raise HTTPException(status_code=resp.status)
            anime = await resp.json()
    
    movie = await ops.get_random_one()
    
    return {"anime": anime["data"], "movie": movie[0]}


@router.get("/", response_model=list[Movie])
async def get_movies(count: int = Query(default=5, alias="count"), ops: OpsForMongo = Depends(db.get_movie_ops)):
    if not 1 <= count <= 25:
        raise HTTPException(status_code=400)
        
    return await ops.get_random(count)
