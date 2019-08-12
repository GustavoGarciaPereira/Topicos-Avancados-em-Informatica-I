valor = int(input("valor far: "))
fat = 1
while valor > 0:
    fat *= valor
    valor -= 1
print("fatorial: ",fat)