from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
class Post(Base):
    __tablename__ = 'posts'
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='True')
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner=relationship("Users")
#Tables for Users registration
class Users(Base):
    __tablename__ = 'users'
    id=Column(Integer,nullable=False,primary_key=True)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
#Vote/Like table
class Vote(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)