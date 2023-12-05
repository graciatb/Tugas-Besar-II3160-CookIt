# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..controller.recipe import *
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

# Activate Router
router = APIRouter(
    prefix = "/recipe",
    tags = ['Recipe']
)

# Get All Recipes
@router.get("/")
def get_recipes(current_user : schemas.User = Depends(oauth2.get_current_user)):
    return allRecipes()

# Create Recipe
@router.post("/", status_code = status.HTTP_201_CREATED)
def create_recipe(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
   return allRecipes()

# Get Latest Recipe
@router.get("/latest")
def get_latest_recipe(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return latestRecipe()

# Get Recipe by Id
@router.get("/{id}")
def get_recipe_by_id(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return idRecipe(id)

# Get Recipe by Category
@router.get("/category/{category}")
def get_recipe_by_category(category: str, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return categoryRecipe(category)

# Delete Own Recipe
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_recipe(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return idRecipe(id) 

# Update Own Recipe
@router.put("/{id}")
def update_recipe(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return idRecipe(id)