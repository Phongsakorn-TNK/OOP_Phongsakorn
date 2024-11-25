val = 0
while True:
    try:
        num = (input("ใส่ราคาสินค้า: "))
        if num == "exit":
            break
        
        num = int(num)
        if num == 0:
            raise ZeroDivisionError
        elif num < 0:
            raise Exception
        else:
            val += num
            print(f"ยอดรวม {val} บาท")
    except ZeroDivisionError:
        print("ราคาสินค้าต้องมากกว่า 0")
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
    except:
        print("ราคาสินค้าต้องไม่ติดลบ")
print(f"ยอดรวมทั้งหมด {val} บาท")