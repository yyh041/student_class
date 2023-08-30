class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.mark = {"语文": 0, "数学": 0, "英语": 0}

    def upload_score(self):
        judge = input("要输入成绩吗: (是/否)")
        while judge != "否":
            course = input("请输入想上传成绩的课程名：")
            self.mark[course] = int(input(f"请输入{self.name}的{course}成绩："))
            judge = input("要输入成绩吗")

    def score(self):
        print(f"""
        {self.name}的语文成绩是{self.mark["语文"]}
        数学成绩是{self.mark["数学"]}
        英语成绩是{self.mark["英语"]}""")


student1 = Student('林思亦', '041')
student1.upload_score()
student1.score()
