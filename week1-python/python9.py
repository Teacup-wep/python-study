s=input("几岁：")
try:
    print(int(s)+1)
except ValueError:
    print("输入非法")
#点餐系统
menu={"鱼":5,"肉":5}
i=0
while True:
    s=input("点：")
    if s=="完":
        break
    i+=menu.get(s,0)
print(f"一共{i}元")
      