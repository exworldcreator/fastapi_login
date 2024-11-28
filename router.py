from fastapi import FastAPI, APIRouter, Depends, HTTPException
from database import fake_users_db, get_user
import models, schemas, database
from security import auth, password
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated

app = FastAPI()
router = APIRouter()

@router.post("/login", response_model = models.LoginResponse)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(fake_users_db, form_data.username)
    if user is None or not password.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )
        
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data = {"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token}