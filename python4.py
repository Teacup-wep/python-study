with open("jobs.txt","w",encoding="utf-8") as f:
    f.write("ai工程师-泉州\n")
    f.write("软件测试师-福州\n")
    f.write("信息采集工程师-厦门\n")
with open("jobs.txt","r",encoding="utf-8") as f:
    con=f.read()
    print(con)
print("-"*20)
with open("jobs.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    print(lines)
    for line in lines:
        clean_line=line.strip()
        if "泉州" in clean_line:
            print(f"泉州是本地岗位{clean_line}")
        else:
            print(f"泉州不是本地岗位{clean_line}")

