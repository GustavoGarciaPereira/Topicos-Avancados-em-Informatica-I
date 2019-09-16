

'''
. Ler uma palavra e uma letra qualquer. 
Mostrar a palavra cortada na primeira posição em que
encontrar a letra informada.
'''

string = input('Informe uma palavra: ')
letra = input('Informe uma letra: ')


# if letra in string:
#     print("letra {} esta na palavra {}".format(letra,string))

print("{}".format(string.split(letra)[0]))