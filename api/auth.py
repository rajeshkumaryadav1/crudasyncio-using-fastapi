from fastapi import APIRouter,status,HTTPException,Depends
from .schemas import LoginSchema
from .db import User,database
from typing import List
from passlib.hash import pbkdf2_sha256
from .tokens import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(
    tags=["Auth"]
)

@router.post('/login/',)
async def login(request:OAuth2PasswordRequestForm = Depends()):
    query=User.select().where(User.c.username==request.username)
    my_user=await database.fetch_one(query=query)
    if not my_user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='username not found')
    if not pbkdf2_sha256.verify(request.password,my_user.password):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="password not found")
    acess_token=create_access_token(data={"sub":my_user.username})
    return {'access_token':acess_token,'token_type':'bearer','data':my_user}
    return my_user

































