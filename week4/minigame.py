import random
win = 0
lose = 0
balance = 0

while True:
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(a)
    print("โปรแกรมเปายิงฉุบ")
    print("เลือก ค้อน กรรไกร กระดาษ")
    val = str(input("คุณเลือก: "))
    if a == val:
        print("ผลลัพท์คือ เสมอ")
        balance += 1
    elif(a == "ค้อน" and val == "กรรไกร"):
        print("ผลลัพท์คือ แพ้")
        lose += 1
    elif(a == "กรรไกร" and val == "กระดาษ"):
        print("ผลลัพท์คือ แพ้")
        lose += 1
    elif(a == "กระดาษ" and val == "ค้อน"):
        print("ผลลัพท์ แพ้")
        lose += 1
    elif(a == "กระดาษ" and val == "กรรไกร"):
        print("ผลลัพท์ ชนะ")
        win += 1
    elif(a == "กระไกร" and val == "ค้อน"):
        print("ผลลัพท์ ชนะ")
        win += 1
    elif(a == "ค้อน" and val == "กระดาษ"):
        print("ผลลัพท์ ชนะ")
        win += 1
    elif val == 'หยุด':
        print("ออกแล้ว")
        print(f"ผลชนะ: {win} แพ้: {lose} เสมอ: {balance}")
        break
    else:
        print("พิมพ์ให้ถูก")
    print("-----------------------")