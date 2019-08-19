import random
'''
2. Escreva um programa que armazene em uma estrutura composta 50 números inteiros e mostre
somente os positivos.
'''

lista = []

for i in range(50):
    lista.append(random.randrange(-25,25))
print(lista)

for i in lista:
    if i > 0:
        print(i)


