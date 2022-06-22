'''
Created on 20 Jun 2022

@author: estudiante
'''
def numberInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if ord(cadena[i])>=48 and ord(cadena[i])<=57:
            contador+=1
        
    return contador

print(numberInString("31infdoa234"))