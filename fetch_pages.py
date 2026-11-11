import requests
url="https://api.bilibili.com/x/web-interface/popular"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ""(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}
for page in range(1,4):
    params={"pn":page,"ps":5}
    r=requests.get(url,headers=headers,timeout=5,params=params)
    if r.status_code !=200:
        print("出错了",r.status_code)
        continue
    data=r.json()
    if data["code"]!=0:
        print("出错了",data["code"])
    v=data["data"]["list"]
    print(f" 第{page}页，共{len(v)}条")
    for i in v:
        print(i["title"], "|", i["owner"]["name"], "|", i["stat"]["view"])
    


