from fastapi import FastAPI


app = FastAPI()

@app.get("/")

def index():
    return {'data':{'name':'lee'}}

@app.get("/about")
def about():
    return {'data':{'name':'lee','age':20}}