'''
Created on 3 Jun 2022

@author: estudiante
'''
def numCaracteres(cadena, caracter):
    contador=0
    encontrado=False
    for i in range(0, len(cadena)):
        if caracter==cadena[i]:
            contador+=1
    return contador

print(numCaracteres("hoohafefe", "h"))
