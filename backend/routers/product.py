from fastapi import status, Depends, APIRouter
from .. import schemas, oauth2
import requests

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get('/')
def get_all_products(token: str = Depends(oauth2.get_current_user_token)):
    url = "https://tst-api-order-production.up.railway.app/products/"
    products = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return products

@router.get('/{id}')
def get_product(id:int, token: str = Depends(oauth2.get_current_user_token)):
    url = f"https://tst-api-order-production.up.railway.app/products/{id}"
    product = requests.get(url, headers={"Authorization": f"Bearer {token}"}).json()
    return product