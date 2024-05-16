from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class UserPublic(BaseModel):
    id: int
    name: str
    
class UserDetail(BaseModel):
    id: int
    name: str
    email: str