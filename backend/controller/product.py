from .auth import getFormat

def allProducts():
    url = "https://tst-api-order-production.up.railway.app/products/"
    return getFormat(url)

def idProduct(id: int):
    url = f"https://tst-api-order-production.up.railway.app/products/{id}"
    return getFormat(url)