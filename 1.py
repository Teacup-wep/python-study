import json, requests

r = requests.get("https://api.bilibili.com/x/web-interface/popular",
                 params={"pn": 1, "ps": 2},
                 headers={"User-Agent": "Mozilla/5.0"})
data=r.json()
print(data['code'])
print("-"*20)
print(data["data"].keys()) 
print("-"*20)
print(len(data["data"]["list"]))  