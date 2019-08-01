preco_tinta = 36.90
largura_parede = float(input("Largura da parede: "))
altura_parede = float(input("Altura da parede: "))



def calculo_area(largura_parede, altura_parede):
    area = (largura_parede * altura_parede)
    return (area*5)/2



valor_pago = calculo_area(largura_parede, altura_parede) * preco_tinta
print("litros de tinta: ",calculo_area(largura_parede, altura_parede))
print("valor pago: ",valor_pago)
