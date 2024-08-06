from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import session
from ..import database,schemas,models,utils
from ..database import get_db
router=APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:session=Depends(get_db)):
    password=utils.hash(user.password)
    user.password = password
    new_user=models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
#Retrieve user's data based on id
@router.get("/{id}",response_model=schemas.UserDetails) 
def get_user(id:int,db:session=Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.id==id).first()
    return user