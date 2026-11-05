jobs=["工程师","测试师 ","实施师"]
print("列表里第一个岗位：",jobs[0] )
jobs.append("产品助理")
print("现在列表：",jobs)
print("一共有：",len(jobs),"个岗位")
print("-"*20)
my={"name":"李华","city":"泉州","major":"软件工程"}
print(f"我的名字:{my['name']}")
print("我的经验是",my.get("experience", "无经验小白"))