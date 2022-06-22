'''
Created on 20 Jun 2022

@author: estudiante
'''

def lowCaseInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if ord(cadena[i])>=97 and ord(cadena[i])<=122:
            contador+=1
        
    return contador

print(lowCaseInString("NNJFiejsNNsdk"))
        
        

