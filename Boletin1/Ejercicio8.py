'''
Created on 31 May 2022

@author: estudiante
'''
def compruebaA(cadena):
    resultado=True
    if len(cadena)<2:
        resultado=False
    else:
        for i in range(0, len(cadena)):
            ascii=ord(cadena[i])
            if ascii<65 or ascii>90:
                resultado=False
    return resultado

def compruebaB(cadena):
    resultado=True
    if len(cadena)<2:
        resultado=False
    else:
        for i in range(0, len(cadena)):
            ascii=ord(cadena[i])
            if ascii<48 or ascii>57:
                resultado=False
    return resultado


cadena=input("Introduce la identificacion de la SS: ")
cadenaAux1=""
cadenaAux2=""
encontrado1=False
encontrado2=False
for i in range(0, len(cadena)):
    if cadena[i]=="-":
        encontrado1=True
    if encontrado1==False:
        cadenaAux1=cadenaAux1+cadena[i]
        
for i in range(0, len(cadena)):
    if encontrado2==True:
        cadenaAux2=cadenaAux2+cadena[i]
    if cadena[i]=="-":
        encontrado2=True

if encontrado1==False or encontrado2==False:
    print("No se encontró el separador")
else:
    if (compruebaA(cadenaAux1) and compruebaB(cadenaAux2)) or (compruebaA(cadenaAux2) and compruebaB(cadenaAux1)):
        print("Correcto")
    else:
        print("Incorrecto")













