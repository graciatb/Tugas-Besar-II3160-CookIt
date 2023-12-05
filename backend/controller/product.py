from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from ..controller.auth import getFormat, postFormat

def allProducts():
    url = "https://tst-api-order-production.up.railway.app/products/"
    return getFormat(url)

def idProduct(id: int):
    url = f"https://tst-api-order-production.up.railway.app/products/{id}"
    return getFormat(url)

def createProduct():
    url = "https://tst-api-order-production.up.railway.app/products/"
    return postFormat(url)