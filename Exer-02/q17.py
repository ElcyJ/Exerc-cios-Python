def desconto(val,des):
    perc = (des/100)
    new = val * perc
    return new
v = float(input("Valor:"))
d = float(input("Desconto:"))
print(desconto(v,d))
