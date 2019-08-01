
segundos = int(input("intome quantos segundos: "))


hora = int((segundos/3600))
minu =  int((segundos -(hora * 3600))/60)
segun = int(segundos % 60)
print("{}h {}min {}s".format(hora, minu, segun))