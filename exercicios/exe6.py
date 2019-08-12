




print("funcao  y = 4x + 3")

xi = int(input("xi: "))
xf = int(input("xf: "))
y = 0
for i in range(xi,xf+1):
    y = (4 * i) + 3
    print("(x={})   y = {}".format(i,y))