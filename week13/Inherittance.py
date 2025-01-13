class Animal:
    def  __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"
    
Animal1 = Animal("ปีเตอร์",10,"ดำ")
print(f"สัตว์ตัวหนึ่งมี{Animal1.showinfo()}")

class Dog(Animal):
    def speak(self):
        return "โฮ่งๆ"
Dog1 = Dog("หมาวัด",5,"ดำ")
print(f"หมาชื่อ {Dog1.name} ร้อง {Dog1.speak()}")
print(f"ข้อมูลหมาตัวที่ 1 คือ {Dog1.showinfo()}")