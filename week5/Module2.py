import Function2
sumup = 0
sumdown = 0
while True:
    num = int(input("ใส่ค่า: "))
    if num > 0:
        sumup = Function2.Fn2(num,sumup,sumdown)
    elif num < 0:
        sumdown = Function2.Fn2(num,sumup,sumdown)
    else:
        break
print(f"ผลรวมของบวก = {sumup}\nผลรวมของลบ = {sumdown}")