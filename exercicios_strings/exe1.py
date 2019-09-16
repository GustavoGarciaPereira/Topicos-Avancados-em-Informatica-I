'''
Escreva um programa que leia uma palavra 
qualquer e conte o número de vogais
'''

print("exe1")

string = input("escreva a palavra: ")
cont = 0
for i in string:
    if i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U':
        cont +=1 

print("quantidade de vogais", cont)