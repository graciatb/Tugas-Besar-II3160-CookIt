from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from ..controller.auth import getFormat, postFormat

def allProducts():
    url = "http://localhost:8000/products/"
    return getFormat(url)

def idProduct(id: int):
    url = f"http://localhost:8000/products/{id}"
    return getFormat(url)

def createProduct():
    url = "http://localhost:8000/products/"
    return postFormat(url)