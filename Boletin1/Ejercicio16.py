'''
Created on 3 Jun 2022

@author: estudiante
'''

def suma(cadena):
    resultado=0
    for i in range(0, len(cadena)):
        if ord(cadena[i])>=48 and ord(cadena[i])<=57:
            resultado=resultado+int(cadena[i])
    return resultado

print(suma("hola 12 que tal 422"))

