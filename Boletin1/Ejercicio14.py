'''
Created on 3 Jun 2022

@author: estudiante
'''


def convertirEntero(cadena):
    resultado=0
    for i in range(0,len(cadena)):
        ascii=ord(cadena[i])
        resultado=resultado+ascii

    return resultado

print(convertirEntero("AA"))










