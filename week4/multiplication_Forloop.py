a = int(input("ใส่ตัวคูณ: "))
for i in range(1,25):
    sum = a * i
    if (sum / 2) % 2 != 0:
        print(f"{a} x {i} = {sum}")