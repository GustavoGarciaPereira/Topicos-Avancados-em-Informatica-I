import random
'''
3. Escreva um programa que leia duas estruturas (A e B) de 10 posições e faça a multiplicação dos
elementos de mesmo índice, colocando o resultado em uma terceira estrutura (C). Mostre os
elementos de C.
'''
A = []
B = []
C = []
for i in range(5):
    A.append(random.randrange(20))
    B.append(random.randrange(20))



print("A = ",A)
print("B = ",B)


for i in range(5):
    C.append(A[i]*B[i])
print("C = ",C)