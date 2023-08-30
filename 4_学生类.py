class Student:
    def __init__(self, name, number, ch_score, ma_score, en_score):
        self.name = name
        self.number = number
        self.ch_score = ch_score
        self.ma_score = ma_score
        self.en_score = en_score

    def score(self):
        print(f"""
        {self.name}的语文成绩是{self.ch_score}
        数学成绩是{self.ma_score}
        英语成绩是{self.en_score}""")


student1 = Student('林思亦', '041', 150, 150, 150)
student1.score()
