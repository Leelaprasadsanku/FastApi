from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config:
        orm_mode = True
        # This is used to tell Pydantic to treat the SQLAlchemy model as a dictionary
        # and convert it to a Pydantic model.
        # It allows us to use the SQLAlchemy model directly in the response model.
    
    
class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True
        # This is used to tell Pydantic to treat the SQLAlchemy model as a dictionary
        # and convert it to a Pydantic model.
        # It allows us to use the SQLAlchemy model directly in the response model.
        
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True
        # This is used to tell Pydantic to treat the SQLAlchemy model as a dictionary
        # and convert it to a Pydantic model.
        # It allows us to use the SQLAlchemy model directly in the response model.
        
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None