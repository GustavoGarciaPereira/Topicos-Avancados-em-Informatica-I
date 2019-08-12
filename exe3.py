


valor_1 = int(input("Primeiro: "))
valor_ra = int(input("razão: "))


for i in range(valor_1, 10):
    print("{} - {} com razão {}".format(i,valor_1, valor_ra))
    valor_1 += valor_ra
    