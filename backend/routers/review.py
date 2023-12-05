# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..controller.review import *
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

# Activate Router
router = APIRouter(
    prefix = "/review",
    tags = ['Review']
)

# Get All Reviews
@router.get("/")
def get_review(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return allReviews()

# Create Review
@router.post("/{recipe_id}", status_code = status.HTTP_201_CREATED)
def create_review(recipe_id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
   return reviewByRecipe(recipe_id) 

# Get Reviews by User Id
@router.get("/user/{user_id}")
def get_review_by_user_id(user_id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return reviewByUser(user_id)

# Get Reviews by Recipe Id
@router.get("/recipe/{recipe_id}")
def get_review_by_recipe_id(recipe_id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return reviewByRecipe(recipe_id)