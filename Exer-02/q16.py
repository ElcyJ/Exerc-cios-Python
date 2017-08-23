def quad(lado):
    area = lado * lado
    per = lado * 4
    return area,per
l = int(input("Digite o lado:"))
print("Area: %d, Perimetro: %d" %quad(l))