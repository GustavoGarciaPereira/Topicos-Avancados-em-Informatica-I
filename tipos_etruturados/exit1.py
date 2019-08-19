'''
1. Escreva um programa que leia e mostre em uma estrutura composta 20 elementos inteiros. A
seguir, conte quantos valores pares existem.
'''

t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
contP = 0
for i in t:
    if i%2 == 0:
        contP += 1

print("Existem {} pares".format(contP))