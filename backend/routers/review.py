# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db
import requests

# Activate Router
router = APIRouter(
    prefix = "/review",
    tags = ['Review']
)

# Get All Reviews
@router.get("/")
def get_review(token: str = Depends(oauth2.get_current_user_token)):
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/"
    reviews = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return reviews

# Create Review
@router.post("/{recipe_id}", status_code = status.HTTP_201_CREATED)
def create_review(recipe_id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/{recipe_id}"
    response = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}).json()
    return response

# Get Reviews by User Id
@router.get("/user/{user_id}")
def get_review_by_user_id(user_id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/user/{user_id}"
    reviews = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return reviews

# Get Reviews by Recipe Id
@router.get("/recipe/{recipe_id}")
def get_review_by_recipe_id(recipe_id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/recipe/{recipe_id}"
    reviews = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return reviews