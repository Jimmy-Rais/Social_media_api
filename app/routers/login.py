

from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
router=APIRouter(
    prefix="/login",
    tags=["Login"]
)
@router.post("/")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:session=Depends(database.get_db)):
    #Retrieve the user based on the email
    user=db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    #Hash the tried password
    #Compare it to the hased password stored in the database
    check=utils.verify(user_credentials.password,user.password)
    if not check:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    jwt_token=oauth2.create_access_token(data={'id':user.id})
    return jwt_token
    #Return a JWT token if the passwords match