# Import Libraries
from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, oauth2
import requests

# Activate Router
router = APIRouter(
    prefix = "/recipe",
    tags = ['Recipe']
)

# Get All Recipes
@router.get("/")
def get_recipes(token: str = Depends(oauth2.get_current_user_token)):
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/"
    recipes = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return recipes

# Create Recipe
@router.post("/", status_code = status.HTTP_201_CREATED)
def create_recipe(request:schemas.RecipeCreate, token: str = Depends(oauth2.get_current_user_token)):
   url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/"
   response = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}, json=request.model_dump()).json()
   return response

# Get Latest Recipe
@router.get("/latest")
def get_latest_recipe(token: str = Depends(oauth2.get_current_user_token)):
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/latest"
    recipe = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return recipe

# Get Recipe by Id
@router.get("/{id}")
def get_recipe_by_id(id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/{id}"
    recipe = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return recipe

# Get Recipe by Category
@router.get("/category/{category}")
def get_recipe_by_category(category: str, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/category/{category}"
    recipe = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return recipe

# Delete Own Recipe
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_recipe(id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/{id}"
    response = requests.delete(url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}).json()
    return response

# Update Own Recipe
@router.put("/{id}")
def update_recipe(id: int, updated_recipe: schemas.RecipeCreate ,token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/{id}"
    response = requests.put(url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}, json=updated_recipe.model_dump()).json()
    return response