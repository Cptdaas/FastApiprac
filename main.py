#hello 
from fastapi import FastAPI 
from typing import Optional 
from pydantic import BaseModel 
import uvicorn

app =FastAPI()

@app.get('/index')
def show():
    return {'data':1}

@app.get("/blog/{id}")
def show(id: int):
    return {"About": id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments for blog with id=id
    return {'data':{'1','2'}}
class Blog(BaseModel):
    title: str
    body: str 
    published_at:Optional[bool]

#post method  == to create something 
@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return {'data':f'Blog is created with title as {request.title}'}
    

if __name__ =="__main__":
    uvicorn.run(app, host='127.0.0.1', port=9000)