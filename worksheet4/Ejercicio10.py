'''
Created on 20 Jun 2022

@author: estudiante
'''

def numPalabras(cadena):
    array=[]
    cadenaAux=""
    for i in range (len(cadena)):
        if cadena[i]!=" ":
            cadenaAux+=cadena[i]
        else:
            if cadenaAux!="":
                array.append(cadenaAux)
                cadenaAux=""
    if cadenaAux!=" " and cadenaAux!="":
        array.append(cadenaAux)
        
    return len(array)

print(numPalabras("  he estudiado    mucho  "))
