def dig(num):
    dez = (num // 10) % 10
    return dez
n = int(input("Num:"))
print(dig(n))