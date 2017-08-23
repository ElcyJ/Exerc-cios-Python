def hora(atual):
    h1 = atual // 1000
    h2 = (atual // 100) % 10
    m = (atual % 1000) % 100
    hora = (h1 * 10) + h2
    min = (hora * 60) + m
    return min
h = int(input("Hora atual:"))
print(hora(h))



