from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: Optional[str]
    
class UserInDb(BaseModel):
    username: str
    hashed_password: str
    
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"