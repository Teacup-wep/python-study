jobs=["工程师","测试师 ","实施师"]
print("列表里第一个岗位：",jobs[0] )
jobs.append("产品助理")
print("现在列表：",jobs)
print("一共有：",len(jobs),"个岗位")
print("-"*20)
my={"name":"李华","city":"泉州","major":"软件工程"}
print(f"我的名字:{my['name']}")
print("我的经验是",my.get("experience", "无经验小白"))
job = {"title": "AI训练师", "city": "泉州", "salary": 10000}
job["lll"]="lklklk"
print(job)
for i in job.keys():
    print(i)
print("-"*20)
for i in job.values():
    print(i)
print("-"*20)
for i,n in job.items():
    print(i,n)
print("-"*20)
my_pc = {"brand": "联想", "ram": 16, "price": 6000}
my_pc["ram"]=17
my_pc["cpu"]="i7"
for i,n in my_pc.items():
    print(f"电脑属性->:{i}:{n}")
print(my_pc)