def inv(num):
    dig1 = num // 100
    dig2 = (num // 10) % 10
    dig3 = (num % 100) % 10
    new = (dig3 * 100) + (dig2 * 10) + dig1
    return new
n = int(input("Num:"))
print(inv(n))