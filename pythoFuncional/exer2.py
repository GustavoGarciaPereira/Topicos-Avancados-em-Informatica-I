#2. Calcular o fatorial de um número


#soma = list(map(lambda x:))

soma = lambda n: 1 if n == 0 else n * soma(n-1)

print(soma(3))
#somatorio = lambda