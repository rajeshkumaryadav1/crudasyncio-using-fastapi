from turtle import title
from fastapi import FastAPI
from . import articles,users,auth
from .db import metadata,database,engine
metadata.create_all(engine)


app=FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.connect()

app.include_router(articles.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/articles/')
async def get_article():
    return {'message':'list of articles'}













