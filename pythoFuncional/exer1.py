#1. Calcular a soma dos n primeiros números inteiros maiores que zero


#soma = list(map(lambda x:))

soma = lambda n: 0 if n < 0 else n + soma(n-1)

print(soma(3))
#somatorio = lambda