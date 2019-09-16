'''
Ler uma palavra qualquer e uma letra qualquer. 
Contar quantas vezes esta letra é encontrada na
palavra.
'''

string = input('Informe uma palavra: ')
letra = input('Informe uma letra: ')


# if letra in string:
#     print("letra {} esta na palavra {}".format(letra,string))

print("A letra {} esta presente {} vez(es) na palavra {}".format(letra,string.count(letra),string))