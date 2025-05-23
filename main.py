from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get("/blog")

def index(limit=10, published:bool=True, sort: Optional[str] = None):
    if published:
        return {'data':f"{limit} published blogs from the db"}
    else:
        return {'data':f"{limit} unpublished blogs from the db"}
   

@app.get("/blog/unpublished")
def unpublished():
    return {'data':"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {'data':id}

@app.get("/blog/{id}/comments")
def comments(id:int):
    return {'data':{'1':'comment 1','2':'comment 2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True
    
@app.post("/blog")
def create_blog(blog: Blog):
    return {'data':f"Blog is created with title as {blog.title} and body as {blog.body} and published status as {blog.published}"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
    