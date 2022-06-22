'''
Created on 20 Jun 2022

@author: estudiante
'''

def vocales(cadena):
    vocales=["a", "e", "i", "o", "u"]
    aux=[]
    contador=0
    for i in range(len(cadena)):
        if cadena[i] in vocales and cadena[i] not in aux:
            aux.append(cadena[i])
            contador+=1
    return contador

print(vocales("hola que tal estas"))
