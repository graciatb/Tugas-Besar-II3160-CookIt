# from fastapi import APIRouter, Depends, status, Response, HTTPException
# import requests
# import json
# from ..controller.auth import getFormat

# def allUserOrders():
#     url = "https://tst-api-order-production.up.railway.app/orders/"
#     return getFormat(url)

# def allOrders():
#     url = "https://tst-api-order-production.up.railway.app/orders/all"
#     return getFormat(url)

# def idOrder(id: int):
#     url = f"https://tst-api-order-production.up.railway.app/orders/{id}"
#     return getFormat(url)