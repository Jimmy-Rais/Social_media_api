from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from .database import SessionLocal, engine,get_db
from . import models,schemas,utils
from sqlalchemy.orm import session
from .routers import post,user,login,vote
from fastapi.middleware.cors import CORSMiddleware
import time
#models.Base.metadata.create_all(bind=engine)
app=FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(login.router)
app.include_router(vote.route)
@app.get("/")
async def root():
 return {"message": "Hello learners!!!!!!!"}
