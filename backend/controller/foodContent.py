# from fastapi import APIRouter, Depends, status, Response, HTTPException
# import requests
# import json
# from ..controller.auth import getFormat

# def allContents():
#     url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/"
#     return getFormat(url)

# def latestContent():
#     url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/latest"
#     return getFormat(url)

# def idContent(id: int):
#     url = f"http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/content/{id}"
#     return getFormat(url)