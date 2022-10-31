from dataclasses import Field
from pydantic import BaseModel


class Anime(BaseModel):
    mal_id: int
    title_english: str | None
    title_japanese: str | None
    title_synonyms: list[str] | None
    title: str | None
    type: str | None
    source: str | None
    status: str | None
    duration: str | None
    synopsis: str | None
    url: str | None
    episodes: int | None
    year: str | None
    airing: bool | None
