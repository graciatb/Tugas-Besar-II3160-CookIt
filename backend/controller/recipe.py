from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from .auth import getFormat

def allRecipes():
    url = "http://localhost:8080/recipe/"
    return getFormat(url)

def latestRecipe():
    url = "http://localhost:8080/recipe/latest"
    return getFormat(url)

def idRecipe(id: int):
    url = f"http://localhost:8080/recipe/{id}"
    return getFormat(url)

def categoryRecipe(category: str):
    url = f"http://localhost:8080/recipe/category/{category}"
    return getFormat(url)