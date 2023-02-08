import requests
import json
import random

def board_api(method, title="", content="", id="", path=""):
    API_HOST = "http://127.0.0.1:8000/api/board/"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "title": f"{title} - {id}",
        "content": f"{content}"
    }
    
    try:
        if method == 'GET':
            if id:
                jwt = signin_api(id=id)['token']['access']
                headers["Authorization"] = f"Bearer {jwt}"
            response = requests.get(url, headers=headers)
            print("response status %r" % response.status_code)
            print("response text %r" % response.text)
            
        elif method == 'POST':
            jwt = signin_api(id=id)['token']['access']
            headers["Authorization"] = f"Bearer {jwt}"
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
            print("response status %r" % response.status_code)
            print("response text %r" % response.text)

    except Exception as ex:
        print(ex)

def signin_api(id, password="test"):
    url = "http://127.0.0.1:8000/api/user/sign-in/"
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "id": f"{id}",
        "password": f"{password}"        
    }
    response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
    return response.json()


user = "test"+str(random.randint(1,100))
title = "Dummy Article"
content = "This is for making bulk log data"
board_api(method='POST', title=title, content=content, id=user)

for i in range(1,55000):
    user = "test"+str(random.randint(1,15000))
    title = "Dummy Article"
    content = "This is for making bulk log data"
    board_api(method='POST', title=title, content=content, id=user)