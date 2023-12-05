from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from ..controller.recipe import *
from ..controller.product import *
from ..controller.order import *
from ..controller.foodKit import *

router = APIRouter(
    prefix = "/foodKit",
    tags = ['FoodKit']
)   

@router.get("/{id}")
def get_recommendations(id: int):
    return getRecommendations(id)

@router.get("/ingredients/{id}")
def get_ingredients(id: int):
    return searchIngredients(id)