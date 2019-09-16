'''
Ler uma palavra e duas letras, toda vez que a 
primeira letra aparecer substituí-la pela segunda.
Apresentar a como resultado a nova palavra
'''


string = input('Informe uma palavra: ')
letra1 = input('Informe uma letra1: ')
letra2 = input('Informe uma letra2: ')
string_r = ''

for i in string:
    if i.upper() == letra1 or i == letra1:
        string_r += letra2
    else:
        string_r += i

print(string_r)