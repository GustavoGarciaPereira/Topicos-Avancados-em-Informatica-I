#3. Calcular a soma do intervalo entre dois números, n1 e n2, informados pelo usuário.
n1 = int(input("n1 :"))
n2 = int(input("n2 :"))


soma = lambda n,n_f: 0 if n > n_f else n_f + soma(n,n_f-1)

print(soma(n1,n2))