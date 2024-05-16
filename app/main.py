import bcrypt
import random
import time
from typing import List
from fastapi import FastAPI, HTTPException
from app.models import User, UserPublic, UserDetail
from db.supabase import create_supabase_client

app = FastAPI()

# Initialize supabase client
supabase = create_supabase_client()

def user_exists(key: str = "email", value: str = None):
    user = supabase.from_("users").select("*").eq(key, value).execute()
    return len(user.data) > 0

# Create a new user
@app.post("/user")
def create_user(user: User):
    try:
        user_email = user.email.lower()  # Convert email to lowercase
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())  # Hash password, ensure bytes

        if user_exists(value=user_email):
            return {"message": "User already exists"}  # Check if user already exists

        # Add user to users table
        response = supabase.from_("users").insert({
            "name": user.name, 
            "email": user_email, 
            "password": hashed_password.decode('utf-8')  # Decode hashed password to string before storing
        }).execute()

        if response:
            return {"message": "User creation success"}
        return {"message": "User created failed"}
        
    except Exception as e:
        print("Error:", e)
        return {"message": "User creation failed", "error": str(e)}

@app.get("/users", response_model=List[UserPublic])
def get_users():
    try:
        response = supabase.from_("users").select("id, name").execute()
        if response.data:
            return response.data
        return []
    except Exception as e:
        print("Error:", e)
        return {"message": "Failed to fetch users", "error": str(e)}
    
@app.get("/user/{user_id}", response_model=UserDetail)
def get_user(user_id: int):
    try:
        delay = random.uniform(0.2, 5.0)
        time.sleep(delay)
        response = supabase.from_("users").select("id, name, email").eq("id", user_id).execute()
        if response.data:
            return response.data[0]
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch user")