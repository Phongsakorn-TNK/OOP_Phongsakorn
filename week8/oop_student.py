class student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grader = {}

    def score(self):
        choice = input("กรุณาเลือกวิชาที่กรอกคะแนน\nM = คณิต\nT = ไทย\nS = วิทย์\nE = อังกฤษ\nC = สังคม\n: ")
        score = int(input("ใส่คะแนน: "))
        grade = self.grade(score)
        if choice == "M":
            self.grader["Math"] = grade
        elif choice == "T":
            self.grader["Thai"] = grade
        elif choice == "S":
            self.grader["Science"] = grade
        elif choice == "E":
            self.grader["English"] = grade
        elif choice == "C":
            self.grader["Social"] = grade

    def grade(self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0
    
    def show(self):
        print("\nข้อมูลนักเรียน")
        print(f"ชื่อ: {self.name}")
        print(f"เลขประจำตัว: {self.id}")
        print(f"อายุ: {self.age} ปี")
        print(f"เกรดเฉลี่ย: {self.grader}")
    
stu1 = student("phet",67319010009,18)

stu1.score()
stu1.show()