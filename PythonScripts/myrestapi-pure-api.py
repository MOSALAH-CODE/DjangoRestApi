import requests

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
    res = requests.post(BASE_URL + END_POINT , data=new_data)    
    if not res.ok:
        return res.text
    
    return res.json()

# get_list()
    
print(create_update())