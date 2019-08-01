'''
R$100, R$50, R$20, R$10, R$5 e R$2. Nesse caso, um saque de R$139 resultaria em 
1 nota de R$100, 1 nota de R$20, 1 nota de R$10, 1 nota de R$5 e 2 notas de R$2.

'''
valor = int(input("Informe o valor desejado:"))
re = [{100: 0}, {20: 0}, {10: 0}, {5: 0}, {2: 0}]
num = 0

while(valor > 0):
    print(valor)
    if 100 <= valor:
        num = re[4][2]
        num += 1
        re[0] = {100:num}
        valor -= 100
    if 20 <= valor:
        num = re[4][2]
        num += 1
        re[1] = {20:num}
        valor -= 20
    if 10 <= valor:
        num = re[4][2]
        num += 1
        re[2] = {10:num}
        valor -= 10
    if 5 <= valor:
        num = re[4][2]
        num += 1
        re[3] = {5:num}
        valor -= 5
    if 2 <= valor:
        num = re[4][2]
        num += 1
        re[4] = {2:num}
        valor -= 2
    num = 0
print("valor:",valor)
print(re)
