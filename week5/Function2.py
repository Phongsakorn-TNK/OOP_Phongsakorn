def Fn2(num,sumup,sumdown):
    while True:
        if num < 0:
            sumdown += num
            print(f"ผลลบรวม = {sumdown}")
            return sumdown
        elif num > 0:
            sumup += num
            print(f"ผลบวกรวม = {sumup}")
            return sumup