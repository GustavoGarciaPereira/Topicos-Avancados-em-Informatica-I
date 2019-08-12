





i = 1
maior = 0
while i > 0:
    print("")
    i = int(input("i: "))
    if i % 2 != 0 and i > maior:
        print("impar: ")
        maior = i



        
if maior == 0:
    print("não fio encontrado numeros impares")
else:
    print("maior impar",maior)
