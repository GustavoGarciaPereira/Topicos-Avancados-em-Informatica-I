'''
Ler uma string e um número inteiro, que representa o 
número de caracteres. Eliminar n caracteres
do início da string e apresentar a string resultante.
'''



string = input('Informe uma palavra: ')
num = int(input('Informe um numero: '))

print(string[:num])