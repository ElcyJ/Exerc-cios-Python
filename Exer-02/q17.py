def desconto(val,des):
    perc = (des/100)
    new = val - perc
    return new
v = input("valor:")
d = input("Desconto:")
print(desconto(v,d))
