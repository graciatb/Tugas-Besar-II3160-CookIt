from fuzzywuzzy import fuzz
from .recipe import *
from .product import *

def getIngredients(recipe_id: int):
    recipe = idRecipe(recipe_id)
    ingredients = recipe["ingredients"]
    return ingredients

def splitIngredients(recipe_id: int):
    ingredients = getIngredients(recipe_id)
    ingredients_list = ingredients.split(",")
    return ingredients_list

def searchIngredients(recipe_id: int):
    recommendation_list = []
    ingredients_list = splitIngredients(recipe_id)
    products = allProducts()
    for ingredient in ingredients_list:
        for product in products:
            if product["product_name"] in ingredient:
                recommendation_list.append(product)
    return recommendation_list
    