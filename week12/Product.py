class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def AddStock(self,Amount):
        if Amount > 0:
            self.__stock += Amount
            print(f"เพิ่มสต็อกแล้ว")
        else:
            print("ใส่จำนวนบวก")

    def ReduceStock(self,Amount):
        if Amount > 0:
            if Amount <= self.__stock:
                self.__stock -= Amount
                print("ลดสต็อกแล้ว")
            else:
                print("ลดสต็อกไม่ได้")
        else:
            print("ใส่จำนวนบวก")

    def EditPrice(self,Edit):
        if Edit >= 0:
            self.__price = Edit
            print("แก้ไขราคาแล้ว")
        else:
            print("ราคาไม่ต่ำกว่า 0 บาท")

    def check(self):
        print(f"--------------\nชื่อสินค้า {self.name}")
        print(f"ราคา: {self.__price} บาท")
        print(f"สต็อก: {self.__stock} ชิ้น\n--------------")

Product1 = Product("เสื้อยืด",200,20)
Product2 = Product("กางเกง",500,40)

Product1.AddStock(30)
Product1.EditPrice(300)

Product1.check()
Product2.check()