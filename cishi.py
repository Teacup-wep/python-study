player = {
    "name": "Teacup",
    "level": 1,
    "attributes": {
        "hp": 100,
        "mp": 50,
        "attack": 10
    }
}
player["level"]=3
player["attributes"]["attack"]+=5

print(f"玩家:{player['name']}\n当前等级:{player['level']}\n攻击力：{player['attributes']['attack']}\n血量：{player['attributes']['hp']}")
print("-"*20)
dev_total = 0
employees = [
    {"name": "张三", "department": "开发部", "salary": 12000},
    {"name": "李四", "department": "测试部", "salary": 9000},
    {"name": "王五", "department": "开发部", "salary": 15000},
    {"name": "赵六", "department": "产品部", "salary": 11000}
]
for i in employees:
    print(f"姓名：{i['name']} 部门：{i['department']} 工资：{i['salary']}")
    if i["department"]=="开发部":
        dev_total+=i['salary']



print(dev_total)
print("-"*20)
text = "apple banana apple orange banana apple"
clean_text=text.split(" ")
fruit_text={}
for fruit in clean_text:
    if fruit in fruit_text:
        fruit_text[fruit]+=1
    else:
        fruit_text[fruit]=1
kkk={**fruit_text,**player}
        


print(kkk)





