import json

import requests
BASE = "http://127.0.0.1:5000/"

print("get".center(60, "-"))
response = requests.get(BASE + "getproduct/pepsi")

res = response.json()

for k, v in res.items():
    print(k, "=>", v)

print("-" * 60)
print("put".center(60, "-"))

response = requests.put(BASE + "getproduct/coke", data={'cat': 'baverage'})
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k,v in info.items():
        print(k, "=>", v)

print("-" * 60)
print("patch".center(60, "-"))
data = {'price' : 5000}

response = requests.patch(BASE + "getproduct/coke", json=json.dumps(data))
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k,v in info.items():
        print(k, "=>", v)

print("-" * 60)
print("post".center(60, "-"))
fanta = {'item': '200 ml bottle', 'price': 20, 'qty': 250}

response = requests.post(BASE + "getproduct/fanta", json=json.dumps(fanta))
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k,v in info.items():
        print(k, "=>", v)

print("-" * 60)

print("delete".center(60, "-"))

response = requests.delete(BASE + "getproduct/thumbs_up")
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k,v in info.items():
        print(k, "=>", v)

print("-" * 60)
