from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Modèle Pydantic
class Item(BaseModel):
    text: str
    is_done: bool = False

# Liste qui stocke les items
items = []

#PARTIE 1 : Route racine
@app.get("/")
def root():
    return {"Hello": "World"}

# PARTIE 2 : POST - ajouter un item
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

# PARTIE 4 : GET - lister les items avec limit
# ⚠️ Cette route DOIT être avant /items/{item_id}
@app.get("/items/", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

# PARTIE 2&3 : GET - récupérer un item par id
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")