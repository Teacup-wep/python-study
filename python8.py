# 原始字符串数据，格式：岗位名称-城市-薪资(单位:k)
raw_data = """
AI应用开发-泉州-15k
Java后端-厦门-12k
软件测试助理-福州-8k
AI训练师-泉州-10k
前端开发-厦门-14k
实施工程师-泉州-9k
数据标注员-未知-6k
AI产品经理-泉州-20k
测试工程师-泉州-11k
"""
def analyze_jobs(raw_text):
        clean_raw_date=raw_text.strip().split("\n")
        clean_raw_date3=[]
        clean_raw_date4=[]
        clean_raw_date5=[]
        clean_raw_date6=[]
        for line in clean_raw_date:
            cleans=line.split("-")
            cleans_job=cleans[0]
            cleans_place=cleans[1]
            cleans_money=int(cleans[2].replace("k",""))
            clean_raw_date2={"工作":cleans_job,"地点":cleans_place,"工资":cleans_money}
            clean_raw_date3.append(clean_raw_date2)
        for i in clean_raw_date3:
                if "未知" in i["地点"]:
                    continue
                else:
                    clean_raw_date4.append(i)
        for i in clean_raw_date4:
            if ("泉州" in i["地点"]) or ("厦门" in i["地点"]):
                    clean_raw_date5.append(i)
        clean_raw_date5.sort(key=lambda x:x["工资"],reverse=True)
        a=0
        for i in clean_raw_date5:
            clean_raw_date6.append(i)
            a=a+1
            if a>=3:
                    break
            for index, job in enumerate(clean_raw_date6):
                  
                print(f"第{index+1}名：{job['工作']} | 城市：{job['地点']} | 薪资：{job['工资']}k")

        return clean_raw_date6
top_jobs = analyze_jobs(raw_data) 
with open("top_jobs.txt", "w", encoding="utf-8") as f:
    # 循环把成品写进文件里
    for index, job in enumerate(top_jobs):
        # 把字典拼成漂亮的字符串，注意最后要加 \n 换行
        text_line = f"第{index+1}名：{job['工作']} | 城市：{job['地点']} | 薪资：{job['工资']}k\n"
        f.write(text_line) # 写进去！

               


       
      
              
    

        
