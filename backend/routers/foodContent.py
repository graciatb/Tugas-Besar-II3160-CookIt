# Import Libraries
from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
import requests

# Activate Router
router = APIRouter (
    prefix = "/content",
    tags = ['Content']
)

# Get All Food Content
@router.get("/")
def get_contents(token: str = Depends(oauth2.get_current_user_token)):
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/"
    all_contents = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return all_contents

# Create Content
@router.post("/", status_code = status.HTTP_201_CREATED)
def create_content(request:schemas.ContentCreate, token: str = Depends(oauth2.get_current_user_token)):
   url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/"
   response = requests.post(url, json=request.model_dump(), headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}).json()
   return response

# Get Latest Food Content
@router.get("/latest")
def get_latest_content(token: str = Depends(oauth2.get_current_user_token)):
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/latest"
    latest_content = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return latest_content

# Get Food Content by Id
@router.get("/{id}")
def get_content_by_id(id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/{id}"
    content = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return content

# Delete Own Food Content
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_content(id: int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/{id}"
    response = requests.delete(url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}).json()
    return response

# Update Own Food Content
@router.put("/{id}")
def update_content(id: int, request:schemas.ContentCreate, token: str = Depends(oauth2.get_current_user_token)):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/{id}"
    response = requests.put(url, headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}).json()
    return response