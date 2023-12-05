from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from ..controller.auth import getFormat

def allUserOrders():
    url = "http://localhost:8000/orders/"
    return getFormat(url)

def allOrders():
    url = "http://localhost:8000/orders/all"
    return getFormat(url)

def idOrder(id: int):
    url = f"http://localhost:8000/orders/{id}"
    return getFormat(url)