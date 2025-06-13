from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def home():
   return {"Data": "Test"}

@app.get("/about")
def about():
   return {"data": "hi"}

inventory = {
   1: {
      "name": "Milk",
      "price" : 34
   }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
   return inventory[item_id]


@app.get("/get-item-by-name")
def get_item(*, name : Optional[str] = None, test: int):
   for i in inventory:
      if inventory[i]["name"] == name:
         return inventory[i]
      return {"Data" : "Not found"}
# !uvicorn app:app --reload

