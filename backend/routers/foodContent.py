# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..controller.foodContent import *
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

# Activate Router
router = APIRouter (
    prefix = "/content",
    tags = ['Content']
)

# Get All Food Content
@router.get("/")
def get_contents(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return allContents()

# Create Content
@router.post("/", status_code = status.HTTP_201_CREATED)
def create_content(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
   return allContents()

# Get Latest Food Content
@router.get("/latest")
def get_latest_content(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return latestContent()

# Get Food Content by Id
@router.get("/{id}")
def get_content_by_id(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return idContent(id)    

# Delete Own Food Content
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_content(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return idContent(id)    

# Update Own Food Content
@router.put("/{id}")
def update_content(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return idContent(id)