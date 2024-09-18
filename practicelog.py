# main.py 
# #hello 
# from fastapi import FastAPI 
# from typing import Optional 
# from pydantic import BaseModel 

# app =FastAPI()

# @app.get('/index')
# def show():
#     return {'data':1}
# # @app.get('/blog')
# # def index(limit=20,published:bool=True):
# #     if published:
# #         return {'data':f'{limit} published Blog from Db list'}
# #     else:
# #         return {"data":f'{limit} blog from database'}
# # @app.get("/blog/{id}")
# # def show(id: int):
# #     return {"About": id}

# # @app.get('/blog/unpublished')
# # def unpublished():
# #     return {'data':'all unpublished blog'}
# # {"detail": [{
# #       "type": "int_parsing",
# #       "loc": ["path","id"],
# #       "msg": "Input should be a valid integer, unable to parse string as an integer",
# #       "input": "unpublished"}]}

# @app.get('/blog/{id}/comments')
# def comments(id):
#     #fetch comments for blog with id=id
#     return {'data':{'1','2'}}

# #post method  == to create something 
# @app.post('/blog')
# def create_blog():
#     return {'data':'Blog is created'}
    