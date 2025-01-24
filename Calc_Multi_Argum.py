def soma (* num):
    s = 0
    for x in num:
        s += x
    return s


x = soma(2,3,4,5,6,7,8,9,10)
print(x)