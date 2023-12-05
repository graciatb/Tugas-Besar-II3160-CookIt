from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from ..controller.auth import getFormat

def allReviews():
    url = "http://localhost:8080/review/"
    return getFormat(url)

def reviewByUser(id: int):
    url = f"http://localhost:8080/review/user/{id}"
    return getFormat(url)

def reviewByRecipe(id: int):
    url = f"http://localhost:8080/review/recipe/{id}"
    return getFormat(url)