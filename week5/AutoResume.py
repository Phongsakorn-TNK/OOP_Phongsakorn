house = {}
human = int(input("จำนวนคนที่จะป้อน: "))
for i in range(1,human+1):
    print(f"กรุณากรอกคนที่ {i}")
    house["nickname"] = str(input("กรุณากรอกชื่อเล่น: "))
    house["No"] = int(input("กรุณากรอกลขที่: "))
    house["Hobby"] = str(input("กรุณากรอกงานอดิเรก: "))
    house["Color"] = str(input("กรุณากรอกสีที่ชอบ: "))
    print(f"ข้อมูลคนที่ {i}\n{house}")
    print("-------------------------------------------")