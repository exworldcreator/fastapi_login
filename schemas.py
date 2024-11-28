from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str
    email: str
    
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    email: str
    
    class Config:
        from_attributes = True