from fastapi import Response, status, HTTPException, Depends, APIRouter
from ..controller.product import *
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, models, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get('/')
def get_all_products(db: Session = Depends(get_db)):
    return allProducts()

@router.get('/{id}')
def get_product(id:int, db: Session = Depends(get_db)):
    return idProduct(id)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_product(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return createProduct()

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_product(id:int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return idProduct(id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int, db: Session = Depends(get_db)):
    return idProduct(id)