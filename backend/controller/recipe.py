from .auth import getFormat

def allRecipes():
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/"
    return getFormat(url)

def latestRecipe():
    url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/latest"
    return getFormat(url)

def idRecipe(id: int):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/{id}"
    return getFormat(url)

def categoryRecipe(category: str):
    url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/category/{category}"
    return getFormat(url)