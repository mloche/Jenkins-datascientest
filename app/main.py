from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello":"We Love datascientest, adn we dit it ! We built a CI-CD pipeline !!"}
