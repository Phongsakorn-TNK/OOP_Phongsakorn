print("โปรแกรมตัดเกรด")
point = int(input("โปรดกรอกคะแนน: "))
if point > 100:
    print("ป้อนไม่เกิน 100")
elif point >= 80:
    print("คุณได้เกรด 4")
elif point >= 70:
    print("คุณได้เกรด 3")
elif point >= 60:
    print("คุณได้เกรด 2")
elif point >= 50:
    print("คุณได้เกรด 1")
elif point < 0:
    print("ป้อนไม่น้อยกว่า 0")
elif point <= 49:
    print("คุณได้เกรด 0")
    solve = str(input("ต้องการแก้ 0 ไหม ตอบ y/n: "))
    if solve == "y":
        print(f"คะแนนที่ขาดคือ {50 - point} คะแนน")
    elif solve == "n":
        print("ติด 0 ไป")
else:
    print("โปรดป้อนค่าที่ถูกต้อง")