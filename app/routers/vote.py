from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import session
from ..import database,schemas,models,oauth2
from ..database import get_db
route=APIRouter(
    prefix="/vote",
    tags=["Votes"]
)
@route.post('/',status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #Check if the post exists,if not raise exception
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {vote.post_id} not found")
    #check if the user has already liked the post
    found_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
    found=found_query.first()
    if (vote.dir==1):
        if found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="You have already voted")
        new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"The vote has been successfully added"}
    else:
        if not found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="You haven't voted yet")
        found_query.delete()
        db.commit() 