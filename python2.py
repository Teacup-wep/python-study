score=75
attendance=0.9
if score>=90 and attendance>=0.9:
    print(f"你的成绩和考勤：{score,attendance}","优秀")
elif score>=60:
    print(f"你的成绩和考勤：{score}","合格")
else:
    print(f"你的成绩和考勤：{score,attendance}","不及格")
