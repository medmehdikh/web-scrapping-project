from pydantic import BaseModel

class Annonce(BaseModel):
    title: str
    price: str
    year: str
    mileage: str
    location: str
    link: str
