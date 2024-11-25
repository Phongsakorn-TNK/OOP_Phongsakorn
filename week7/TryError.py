try:
    num = int(input("ใส่ยอดสั่งซื้อ: "))
    if num == 0:
        raise ZeroDivisionError
    elif num < 0:
        raise Exception
    elif num >= 5000:
        count1 = num * 0.2
        print(f"คุณได้ส่วนลด 20% {count1} บาท")
        print(f"ยอดที่ต้องจ่าย {num - count1} บาท")
    elif num >= 2000:
        count2 = num * 0.1
        print(f"คุณได้ส่วนลด 10% {count2} บาท")
        print(f"ยอดที่ต้องจ่าย {num - count2} บาท")
    else:
        print(f"คุณไม่ได้รับสวนลด")
        print(f"ยอดที่ต้องจ่าย {num} บาท")
except ZeroDivisionError:
    print("ใส่เลข 0 ไม่ได้")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except:
    print("ใส่ค่าติดลบไม่ได้")