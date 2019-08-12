

denominador = 1
numerador = 1000
resultado = 0

while denominador <= 50:
    resultado = numerador/denominador
    numerador -= 3
    print("{} ",numerador)
    if numerador %2 != 0:
        resultado -= numerador/denominador
        print("-{}/{}".format(numerador, denominador))
        print("re ",resultado)
    else:
        resultado += numerador/denominador
        print("+{}/{}".format(numerador, denominador))
        print("re ",resultado)
    #print("i",resultado)
    #print("{}/{}".format(numerador, denominador))
    print("re ",resultado)
    denominador+=1