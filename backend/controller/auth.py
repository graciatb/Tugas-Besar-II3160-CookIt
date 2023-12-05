import requests

def getToken():
    url = 'http://127.0.0.1:8000/login'
    data = {"username": "admin@gmail.com", "password": "admin"}
    response = requests.post(url, data=data)
    jsonresponse = response.json()
    bearertoken = str(jsonresponse['access_token'])
    return bearertoken

def getFormat(url: str):
    link = url
    headers = {"Authorization": f'Bearer {getToken()}'}
    response = requests.get(link, headers=headers)
    jsonresponse = response.json()
    return jsonresponse

def postFormat(url: str, data: dict):
    link = url
    headers = {"Authorization": f'Bearer {getToken()}'}
    response = requests.post(link, headers=headers, data=data)
    jsonresponse = response.json()
    return jsonresponse