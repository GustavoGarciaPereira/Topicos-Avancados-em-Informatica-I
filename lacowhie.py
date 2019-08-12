'''
contador = 0
while contador < 5:
    print("valor do contador", contador)
    contador += 1
else:
    print("valor qunado saiu", contador)
print("saiu")
'''


'''
contador = 0
while contador < 5:
    contador += 1
    if contador == 2:
        print("pula")
        continue
    print("valor do contador:",contador)
print("Saiu do laco while")
'''

contador = 0
while contador < 5:
    
    print("contador: ", contador)
    contador += 1
    if contador == 3:
        print("saiu do laco")
        break
print("fora do laco")
