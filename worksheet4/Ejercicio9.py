'''
Created on 20 Jun 2022

@author: estudiante
'''
vocales=["a", "e", "i", "o", "u"]

def ejercicio9(cadena):
    cadenaNueva=""
    for i in range(len(cadena)):
        if cadena[i] not in vocales and cadena[i]!=" ":
            cadenaNueva+=cadena[i]
    for i in range(len(cadena)):
        if cadena[i] in vocales and cadena[i]!=" ":
            cadenaNueva+=cadena[i]   
    return cadenaNueva

print(ejercicio9("hola que tal estas"))     
    