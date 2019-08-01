valor_mensalidade  = float(input("valor_mensalidade: "))
percentual_reajuste = float(input("percentual_reajuste: "))

def calculo_percetual(valor_mensalidade, percentual_reajuste):
    return (percentual_reajuste * valor_mensalidade)/100

print(calculo_percetual(valor_mensalidade, percentual_reajuste))