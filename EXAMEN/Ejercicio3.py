'''
Created on 22 Jun 2022

@author: estudiante
'''

def cambiarLetra(cadena, letra1, letra2):
    resultado=""
    for i in range(len(cadena)):
        caracter=cadena[i]
        if caracter==letra1:
            caracter=letra2
        resultado+=caracter
    return resultado

print(cambiarLetra("maria", "a", "o"))