#4. Calcule o resultado da operação de um número x elevado à potência y.

elevado = lambda x,n: 1 if n == 0 else x * elevado(x,n-1)

print(elevado(2,2))
