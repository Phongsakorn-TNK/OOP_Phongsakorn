import random
class Student:
    def __init__(self,name,nickname):
        self.name = name
        self.nickname = nickname
        self.score = 0
        self.grade = ""

    def exam(self):
        self.score = random.randint(1,10)

    def Grade(self):
        if self.score >= 5:
            self.grade = "สอบผ่าน"
        else:
            self.grade = "สอบไม่ผ่าน"

Std1 = Student("ตรีมิตร บุญตะคำ","ดรีมมี่")
Std1.exam()
Std1.Grade()

Std2 = Student("ปิติพงค์ ภูมิพงศ์","ปอน")
Std2.exam()
Std2.Grade()

Std3 = Student("เตชิน ศรีพุฒ","ไปรท์")
Std3.exam()
Std3.Grade()

Std4 = Student("ตรีมิตร บุญตะคำ","ดรีมมี่")
Std4.exam()
Std4.Grade()

Std5 = Student("ชลันบาส ธราพร","การ์ดโบว์")
Std5.exam()
Std5.Grade()

AllStd = [Std1,Std2,Std3,Std4,Std5]
for i in AllStd:
    print(f"ชื่อ: {i.name} ชื่อเล่น: {i.nickname} สอบได้ {i.score} คะแนน {i.grade}")