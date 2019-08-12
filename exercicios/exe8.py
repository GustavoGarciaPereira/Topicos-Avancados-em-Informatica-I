



maior = 0
valor = 0
i = 0
contaMa = 0
contaMe = 0
controle = 0
menor = 0
lista = []

while i < 7:
    valor = int(input("valor: "))
        

    if valor > maior:
        maior = valor
        contaMa += 1
        print("fora de ordem crescente")


        
    if valor < menor:
        menor = valor
        contaMe += 1
        print("fora de decrescente")


        
    
    lista.append(valor)
    i+=1


for i in range(len(lista)):
    if lista[i] != lista[0]:
        print("Não são todos iguais")
        break
else:
    print("todos iguais!")
