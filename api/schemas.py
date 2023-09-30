from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# **************************************    User Schema   ********************************************
class User(BaseModel):

    first_name:str
    last_name:str
    username:str
    email:EmailStr
    password:str
    control:str="user"

class UserResponse(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:EmailStr
    control:str

    class Config:
        orm_mode = True


# **************************************    Post Schema   ********************************************

class Product(BaseModel):
    name:str
    barcode:str
    brand:str
    description:str
    price:float
    available:bool=True
    admin_name:str

class ProductRes(BaseModel):
    name:str
    barcode:str
    brand:str
    description:str
    price:float
    available:bool=True    

    class Config:
        orm_mode=True


# **************************************    Votes Schema   ********************************************

class Review(BaseModel):
    username:str
    product_id:str
    user_review:str
    user_rating:int

    
class ReviewRes(BaseModel):
    username:str
    user_review:str
    user_rating:int

    class Config:
        orm_mode=True
        
# **************************************    JWT Schema   ********************************************

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class LoginResponse(BaseModel):
    secret_key:str
    token:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:str