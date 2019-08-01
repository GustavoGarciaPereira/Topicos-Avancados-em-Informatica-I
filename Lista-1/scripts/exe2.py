comprimento  = float(input("comprimento: "))
largura = float(input("largura: "))
altura = float(input("altura: "))


def cal(comprimento,largura,altura):
    return 2*(largura*altura) + 2*(comprimento*altura)

print(cal(comprimento,largura,altura)/1.5)