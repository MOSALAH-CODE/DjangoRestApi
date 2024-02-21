import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "api/updates/"

def get_list():
    res = requests.get(BASE_URL + END_POINT)
    if  not res.ok:
        raise Exception("Couldn't retrieve the list of updates")
    print(res.json())

def create_update():
    new_data = {
        "user": 1,
        "content": "hi there"
    }
    res = requests.post(BASE_URL + END_POINT , data=json.dumps(new_data))    
    if not res.ok:
        return res.text
    
    return res.json()

def do_obj_update():
    new_data = {
        "user": 1,
        "content": "new update 123", 
    }
    res = requests.put(BASE_URL + END_POINT + "1/", data=json.dumps(new_data))   # Updating object with id 1
    if not res.ok:
        return res.text
    
    return res.json()

def do_obj_delete():
    res = requests.delete(BASE_URL + END_POINT + "1/")   # Deleting object with id 1
    if not res.ok:
        return res.text
    
    return res.json()

    
# print(create_update())

# print(do_obj_update())

# get_list()

print(do_obj_delete())

get_list()
