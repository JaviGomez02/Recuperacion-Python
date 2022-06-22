'''
Created on 20 Jun 2022

@author: estudiante
'''

def upperCaseInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if ord(cadena[i])>=65 and ord(cadena[i])<=90:
            contador+=1
        
    return contador

print(upperCaseInString("HoidHeusKLees"))