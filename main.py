from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Funcionamiento de DTO

class Item(BaseModel):
    name: str = None
    price: float = None
    is_offer: bool | None = None

@app.get("/")
async def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price, "item_offer": item.is_offer}