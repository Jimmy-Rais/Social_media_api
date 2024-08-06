from datetime import datetime
from pydantic import BaseModel, conint
from pydantic import EmailStr
class Post(BaseModel):
    title:str
    content:str
    #Optional field
    published: bool =True
    #Retrieve User Response
class UserDetails(BaseModel):
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode = True
#Create User
class CreatePost(BaseModel):
    title:str
    created_at:datetime
    owner_id:int
    owner:UserDetails
    class Config:
        orm_mode = True
        
#Update User
#New User
class UserCreate(BaseModel):
    email:EmailStr
    password:str
#New User Response
class UserOut(BaseModel):
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode = True

#Update Post Response
class PostUpdate(BaseModel):
    title:str
    content:str
    created_at:datetime
#User login
class UserCredentials(BaseModel):
    email:EmailStr
    password:str
#Token verification schemas
class Token(BaseModel):
    token:str
    tokentype:str
class TokenData(BaseModel):
    id:str
#Vote/like schemas
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1) # type: ignore
    