def Fn1(num1,num2):
    result = []
    for i in range(num1,num2+1):
        if i % 3 != 0:
            result.append(i)
    return result