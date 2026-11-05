jobs=["工程师","测试师 ","实施师"]
for job in jobs:
    print(f"岗位:{job}")
for i in range(5):
    print(f"次数：{i}")
for job2 in jobs:
    if "测试" in job2:
        print("找到了")
    else:
        print(" 没找到")
print("-"*20)
for i in range(10):
    if i==3:
        print(f"找到3了")
        break
    print(f"此时i等于：{i}")
for i in range(10):
    if i==3:
        print(f"找到3了")
        continue
    print(f"此时i等于：{i}")
