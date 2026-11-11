def check_job(keyword):
    print(f"正在帮你检查包含{keyword}的岗位")
    if "AI" in keyword:
        result = "这是 AI 相关的潜力岗！"
    else:
        result = "这是传统岗位。"
        return result
with open("jobs_data.txt","w",encoding="utf-8") as f:
    f.write("AI应用开发工程师 | 泉州 | Python, API\n")
    f.write("Java后端开发 | 厦门 | Java, MySQL\n")
    f.write("AI测试工程师 | 泉州 | 自动化, 测试用例\n")
    f.write("前端开发 | 福州 | Vue, 微信小程序\n")  
with open("jobs_data.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    i=0
    for line in lines:
        clean_line=line.strip()

        if "泉州" in clean_line and "AI" in clean_line:
            print(f"完美匹配泉州岗位{clean_line}")
            i=i+1
        elif "泉州" in clean_line:
            print(f"备选泉州岗位{clean_line}")
            i=i+1
        else:
            print("直接忽略")
        if i>=2:
            print("泉州好岗位找够了，停止搜索！")
            break
    

        