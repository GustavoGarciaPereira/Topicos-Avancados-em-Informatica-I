


'''. Escreva um programa que leia uma palavra qualquer e veri que se esta palavra é um
palíndromo.'''


string = input('Informe uma palavra: ')

if string == string[::-1]:
    print("É palindromo!")
else:
    print("Não é palindromo!")