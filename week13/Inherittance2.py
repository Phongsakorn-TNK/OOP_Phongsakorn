class Animal:
    def  __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"

class Dog(Animal):
    def __init__(self, name, age, color,race):
        super().__init__(name, age, color)
        self.race = race
    def showdog(self):
        return f"หมาพันธุ์ {self.race} มี {super().showinfo()}"

Dog1 = Dog("บาส",5,"ดำ","บ้าน")
print(Dog1.showdog())