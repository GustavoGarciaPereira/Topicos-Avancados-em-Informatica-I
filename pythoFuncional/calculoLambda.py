cubo = lambda x: x * x * x
print(cubo(2))

soma = lambda x,y: x  + y
print(soma(2,3))

soma_2 = lambda x,y: print("soma: ",soma(x,y))
soma_2(2,3)

operacao = lambda x,y,o: o(x,y)
operacao(2,6,soma_2)

f = list(map(lambda x: x**2,[2,3,4,5,6,7]))
print(f)

t = list(map(lambda x,y: x**y,[1,2,3,4],[1,2,3,4]))
print(t)

c = list(map(lambda x,y:[x**2,str(y)],[10,11,12,13,14],['a',3,10.5,'agua',200]))
print(c)