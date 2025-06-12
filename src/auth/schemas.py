from pydantic import BaseModel, Field
import uuid 
from datetime import datetime 

class UserModel(BaseModel):
    uid: uuid.UUID 
    first_name: str
    last_name: str
    username: str 
    email: str 
    password_hash: str = Field(exclude=True)
    is_verified: bool
    created_at: datetime
    updated_at: datetime 
    
class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    email: str = Field(max_length=50)
    username: str = Field(max_length=8)
    password: str = Field(min_length =8, max_length=12) 
    
class UserLoginModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=8, max_length=12)