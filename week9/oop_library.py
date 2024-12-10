class Library:
    def __init__(self):
        self.book = {}
    
    def add_book(self):
        while True:
            bookname = input("ใส่ชื่อหนังสือ: ")
            if bookname == "exit":
                print("ยกเลิกการเพิ่ม\n")
                break
            else:
                author = input("ใส่ชื่อคนแต่ง: ")
                page = (input("ใส่จำนวนหน้า: "))
                price = (input("ใส่ราคา: "))
                self.book[bookname] = {
                    "author": author,
                    "page": page,
                    "price": price
                }
                print(f"เพิ่มหนังสือ {bookname} แล้ว")

    def show_books(self):
        print("รายชื่อหนังสือในห้องสมุด")
        for bookname, details in self.book.items():
            print(f"ชื่อหนังสือ: {bookname}")
            print(f"ชื่อผู้แต่ง: {details["author"]}")
            print(f"จำนวนหน้า: {details["page"]} หน้า")
            print(f"ราคา: {details["price"]} บาท\n")


    def find_book(self):
        while True:
            bookname = input("ใส่ชื่อหนังสือที่ต้องการค้นหา: ")
            if bookname == "exit":
                print("ยกเลิกค้นหาหนังสือ")
                break
            elif bookname in self.book:
                details = self.book[bookname]
                print(f"พบหนังสือ {bookname}")
                print(f"ผู้แต่ง: {details["author"]}")
                print(f"จำนวนหน้า: {details["page"]} หน้า")
                print(f"ราคา: {details["price"]} บาท\n")
            else:
                print("ไม่พบหนังสือ")

Book1 = Library()
Book1.add_book()
Book1.show_books()
Book1.find_book()