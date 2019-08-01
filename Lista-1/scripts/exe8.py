


#coeficientes
A = float(input("Coeficiente A: "))
B = float(input("Coeficiente B: "))
C = float(input("Coeficiente C: "))
D = float(input("Coeficiente D: "))
E = float(input("Coeficiente E: "))
F = float(input("Coeficiente F: "))


def calculo_x(A,B,C,D,E,F):
    x = (C*E - B*F)/(A*E - B*D)
    return x

def calculo_y(A,B,C,D,E,F):
    y = (A*F - C*D)/(A*E - B*D)
    return y

x = calculo_x(A,B,C,D,E,F)
y = calculo_y(A,B,C,D,E,F)
print("x = {} y = {}".format(x,y))