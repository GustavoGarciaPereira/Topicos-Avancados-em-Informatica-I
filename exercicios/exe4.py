
valor1 = int(input("primeiro valor: "))
valor2 = int(input("Ultimo valor: "))
valor_potencia = int(input("valor potência: "))


for i in range(valor1, valor2+1):
    print("i = {}^{}  = {}".format(i,valor_potencia,(i ** valor_potencia)))