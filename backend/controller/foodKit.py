from fuzzywuzzy import fuzz
from .recipe import *
from .product import *
import random

def getIngredients(recipe_id: int):
    recipe = idRecipe(recipe_id)
    ingredients = recipe["ingredients"]
    return ingredients

def splitIngredients(recipe_id: int):
    ingredients = getIngredients(recipe_id)
    ingredients_list = ingredients.split(",")
    return ingredients_list

def getSimilarity(ingredient: str, product: str):
    return fuzz.ratio(ingredient, product)

def searchIngredients(recipe_id: int):
    recommendation_list = []
    ingredients_list = splitIngredients(recipe_id)
    products = allProducts()
    for ingredient in ingredients_list:
        for product in products:
            if getSimilarity(ingredient, product["product_name"]) > 45:
                recommendation_list.append(product)
    return recommendation_list

def getRecommendations(recipe_id: int):
    recommendation_list = searchIngredients(recipe_id)
    count = len(recommendation_list)
    if count > 5:
        recommendation_list = random.sample(recommendation_list, 5)
    return recommendation_list