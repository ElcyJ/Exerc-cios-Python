def saque(valor):
    n50 = valor/50
    n10 = (valor%50)/10
    n5 = (valor%10)/5
    n1 = (valor%5)/1
    return n50,n10,n5,n1
v = int(input("Digite o valor a ser sacado:"))
print("%d notas de 50, %d notas de 10, %d notas de 5 e %d notas de 1." %(saque(v)))
