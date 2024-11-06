value = int(input("ใส่ตัวคูณ: "))
i = 1
while i < 25:
    sum = value * i
    if (sum / 2) % 2 != 0:
        print(f"{value} x {i} = {sum}")
    i +=1