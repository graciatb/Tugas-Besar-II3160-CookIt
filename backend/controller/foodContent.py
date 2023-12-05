from fastapi import APIRouter, Depends, status, Response, HTTPException
import requests
import json
from ..controller.auth import getFormat

def allContents():
    url = "http://localhost:8080/content/"
    return getFormat(url)

def latestContent():
    url = "http://localhost:8080/content/latest"
    return getFormat(url)

def idContent(id: int):
    url = f"http://localhost:8080/content/{id}"
    return getFormat(url)