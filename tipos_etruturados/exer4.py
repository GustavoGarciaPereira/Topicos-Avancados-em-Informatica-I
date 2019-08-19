'''
4. Ler e armazenar 30 elementos inteiros em uma estrutura composta. Encontre e mostre o menor
elemento e a sua posição.
'''

lis = [5,3,7,8,0,21,4]

def inx(lis,o):
    for i in lis:
        if o == min(lis):
            return i-1



print("O Menor elemento da lista é ",min(lis))
print("O Menor elemento da lista é ",inx(lis,min(lis)))