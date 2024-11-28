from models import UserInDb

fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": "$2b$12$KIXCg1.qZCl7/En2Q1UBCeMh2l/aOiLRcgt5/ZczXnXo9GpIfphqO",
    }
}

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDb(**user_dict)
    return None