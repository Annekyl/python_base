filename = input("请输入文件名：")
f = open(filename, "a")
stu = input("请输入学生学号，姓名，语文成绩：")
while stu != '':
    stu = stu + '\n'
    f.write(stu)
    stu = input("请输入学生学号，姓名，语文成绩：")
f.close()
