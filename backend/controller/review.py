# from fastapi import APIRouter, Depends, status, Response, HTTPException
# import requests
# import json
# from ..controller.auth import getFormat

# def allReviews():
#     url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/"
#     return getFormat(url)

# def reviewByUser(id: int):
#     url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/user/{id}"
#     return getFormat(url)

# def reviewByRecipe(id: int):
#     url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/review/recipe/{id}"
#     return getFormat(url)