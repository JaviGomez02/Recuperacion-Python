'''
Created on 20 Jun 2022

@author: estudiante
'''
def charactersInString(cadena, caracter):
    num=ord(caracter)
    contador=0
    for i in range(len(cadena)):
        if ord(cadena[i])==num or ord(cadena[i])==(num-32):
            contador+=1
    return contador


print(charactersInString("Hola que hhhaces", "h"))
    