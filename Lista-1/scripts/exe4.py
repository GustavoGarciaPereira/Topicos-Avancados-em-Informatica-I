

def quilometros_andou(odometro_inicio_dia,odometro_final_dia):
    return(odometro_final_dia - odometro_inicio_dia)



valor_combustivel = float(input("valor do combustível: "))
odometro_inicio_dia = float(input("marcação do odômetro no início do dia: "))
odometro_final_dia = float(input("marcação do odômetro no início do final: "))
litros_combustivel = float(input("número de litros de combustível gasto:"))
valor_total = float(input("valor total (R$) recebido dos passageiros"))


consumo = quilometros_andou(odometro_inicio_dia,odometro_final_dia) / litros_combustivel

valor_pago_combustivel = consumo * valor_combustivel

lucro = valor_total - valor_pago_combustivel


print("consumo: ",consumo)
print("valor_pago_combustivel: ",valor_pago_combustivel)
print("lucro: ",lucro)
print("quilometros rodados: ",quilometros_andou(odometro_inicio_dia,odometro_final_dia))