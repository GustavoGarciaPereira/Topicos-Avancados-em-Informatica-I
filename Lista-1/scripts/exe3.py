numero_eleitores = int(input("Numero eleitores: "))
votos_brancos = int(input("Numero votos brancos: "))
votos_nulos = int(input("Numero votos nulos: "))
votos_validos = int(input("Numero votos validos: "))



def regra_tres(numero_eleitores,TV):
    return ((TV*100)/numero_eleitores)


print("",regra_tres(numero_eleitores,votos_brancos))
print("",regra_tres(numero_eleitores,votos_nulos))
print("",regra_tres(numero_eleitores,votos_validos))

print("{}".format(regra_tres(numero_eleitores,votos_brancos)+regra_tres(numero_eleitores,votos_nulos)+regra_tres(numero_eleitores,votos_validos)))
