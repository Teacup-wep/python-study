
all_jobs = [{"工作": line.split("-")[0], "地点": line.split("-")[1], "工资": int(line.split("-")[2].replace("k", ""))} for line in clean_raw_date]

# 2. 一行搞定双重过滤（排除未知，且必须是泉州或厦门）
valid_jobs = [job for job in all_jobs if job["地点"] != "未知" and ("泉州" in job["地点"] or "厦门" in job["地点"])]

# 3. 排序
valid_jobs.sort(key=lambda x: x["工资"], reverse=True)

# 4. 用切片直接拿前三个，连 for 循环和 break 都省了！
top3 = valid_jobs[:3]

# 5. 打印
for index, job in enumerate(top3):
    print(f"第{index+1}名：{job['工作']} | 城市：{job['地点']} | 薪资：{job['工资']}k")




