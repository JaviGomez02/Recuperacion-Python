'''
Created on 3 Jun 2022

@author: estudiante
'''


cadena=input("Introduce la cadena a cifrar: ")
valor=int(input("Introduce el numero: "))

cadenaNueva=""
for i in range (0, len(cadena)):
    ascii=valor+ord(cadena[i])
    while ascii>90:
        ascii=ascii-25
    cadenaNueva=cadenaNueva+chr(ascii)

print(cadenaNueva)


