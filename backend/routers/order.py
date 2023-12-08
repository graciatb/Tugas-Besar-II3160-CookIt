from fastapi import status, Depends, APIRouter
from .. import schemas, oauth2
import requests


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.get('/')
def get_all_users_orders(token: str = Depends(oauth2.get_current_user_token)):
    url = "https://tst-api-order-production.up.railway.app/orders/"
    orders = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return orders

@router.get('/all')
def get_all_orders(token: str = Depends(oauth2.get_current_user_token)):
    url = "https://tst-api-order-production.up.railway.app/orders/all"
    orders = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return orders

@router.get('/{id}')
def get_order(id:int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"https://tst-api-order-production.up.railway.app/orders/{id}"
    order = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return order

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_order(request: schemas.Order, token: str = Depends(oauth2.get_current_user_token)):
    url = "https://tst-api-order-production.up.railway.app/orders/"
    response = requests.post(url, headers = {"Authorization": f"Bearer {token}", "Content-Type":"application/json"}, json=request.model_dump()).json()
    return response