def troc(a,b):
    c = a
    a = b
    b = c
    return a,b
a = input("A:")
b = input("B:")
print("A:%s B:%s" %troc(a,b))
