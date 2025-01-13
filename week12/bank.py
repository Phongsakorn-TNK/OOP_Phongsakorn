class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.__balance += amount
            print(f"คุณได้ฝากเงิน {amount} บาทแล้ว")
        else:
            print("ฝากเงินขึ้นต่ำ 100 บาท")
    def withdraw(self,amount):
        if amount >= 100:
            self.__balance -= amount
            print(f"คุณได้ถอนเงิน {amount} บาทแล้ว")
        else:
            print("ถอนเงินขึ้นต่ำ 100 บาท")
    def check(self):
        return self.__balance

id1 = Bank(1,"Phet",5000)
id1.withdraw(200)
print(f"ยอดเงินของคุณ {id1.name} มีอยู่ {id1.check()} บาท")