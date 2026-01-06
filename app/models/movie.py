from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    title:str
    genres:List[str]
