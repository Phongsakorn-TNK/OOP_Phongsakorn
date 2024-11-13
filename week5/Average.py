box = []
Val = int(input("ต้องการป้อนทั้งหมดกี่ตัว: "))
for i in range(1,Val+1):
    num = int(input(f"ใส่ตัวที่ {i}: "))
    box.append(num)
print(f"ค่าเฉลี่ยของ {box} = {sum(box)/Val}")