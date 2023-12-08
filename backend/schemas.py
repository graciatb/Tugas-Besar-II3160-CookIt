from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config():
        from_attributes = True

class UserCreate(BaseModel): 
    email: EmailStr
    password: str

    class Config():
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class FoodContentBase(BaseModel):
    title: str
    desc: str
    topic: str
    published: bool = True

class ContentCreate(FoodContentBase):
    pass

class Order(BaseModel):
    product_id: int
    quantity: int

class RecipeBase(BaseModel):
    id: int
    title: str
    level: str
    category: str
    ingredients: str
    directions: str
    published: bool = True

class RecipeCreate(BaseModel):
    title: str
    level: str
    category: str
    ingredients: str
    directions: str
    published: bool = True