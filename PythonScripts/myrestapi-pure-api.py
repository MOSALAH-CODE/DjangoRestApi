import requests

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "api/updates"

def get_list():
    res = requests.get(BASE_URL + END_POINT)
    if  not res.ok:
        raise Exception("Couldn't retrieve the list of updates")
    print(res.json())

def create_update():
    new_data = {
        "user": 1,
        "content": "new update"
    }

    res = requests.post(BASE_URL + END_POINT, data=new_data)
    print(res.headers)
    if not res.ok:
        # print(res.text)
        print(res.status_code)
        raise Exception("Couldn't create a new update")
    
    print("Created an update with id", res.json()["id"])

# get_list()
    
create_update()