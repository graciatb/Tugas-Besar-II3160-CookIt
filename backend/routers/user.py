# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..controller.user import *
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
import requests


# Activate Router
router = APIRouter(
    prefix = "/users",
    tags = ['Users']
)

# Create User
@router.post("/", status_code = status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db), ):
    return create(user, db)

# Get User
@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return get(id, db)

# Delete User
@router.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return delete(id, db)