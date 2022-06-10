import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"

def post_data():
    data = {'name':'rajiv',
            'roll':113,
            'city':'kashmir'}
    json_data = json.dumps(data)
    r = requests.post(url = URL , data = json_data)
    data = r.json()
    print(data)
post_data()

def update_data():
    data={'id':1,'name':'vi','roll':210,'city':'york'}
    json_data = json.dumps(data)
    r = requests.put(url = URL , data = json_data)
    data = r.json()
    print(data)
# update_data()