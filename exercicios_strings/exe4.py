'''Ler duas palavras e compará-las. 
O programa deve informar se as palavras são iguais, em
caso
contrário, informar se a primeira é maior do que a segunda, 
se a segunda é maior do que a
primeira ou se são diferentes e tem o mesmo tamanho.
'''

string1 = input('Informe uma palavra1: ')
string2 = input('Informe uma palavra2: ')


if len(string1) == len(string2):
    print("São iguais")
elif(len(string1) > len(string2)):
    print("Primeria e maior que a segunda")
else:
    print("Segunda e maior que a primeira")
    
