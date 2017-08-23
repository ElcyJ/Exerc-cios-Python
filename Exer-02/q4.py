def hora(min):
    hora = min / 60
    min2 = min % 60
    return "%d horas e %d minutos" % (hora, min2)


print(hora(80))