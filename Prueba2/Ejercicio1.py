'''
Created on 7 Jun 2022

@author: estudiante
'''

def fuerteDebil(cadena):
    tieneMayuscula=False
    tieneMinuscula=False
    tieneDigito=False
    resultado=False
    if len(cadena)>=8:
        for i in range(0, len(cadena)):
            num=ord(cadena[i])
            if num>=65 and num<=90:
                tieneMayuscula=True
            if num>=97 and num<=122:
                tieneMinuscula=True
            if num>=49 and num<=57:
                tieneDigito=True
        if tieneDigito and tieneMayuscula and tieneMinuscula:
            resultado=True
    return resultado

print(fuerteDebil("aaaaaaaaaaaaaaaaaaaaaaaaaaa22"))