from fastapi import Response, status, HTTPException, Depends, APIRouter
from ..controller.order import *
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, models, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.get('/')
def get_all_users_orders(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return allUserOrders()

@router.get('/all')
def get_all_orders(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return allOrders()  

@router.get('/{id}')
def get_order(id:int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return idOrder(id)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_order(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return allUserOrders()