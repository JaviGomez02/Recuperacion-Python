'''
Created on 20 Jun 2022

@author: estudiante
'''
def ejercicio7(cadena, palabraBuscar, palabraNueva):
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
        
    for i in range(len(array)):
        if array[i]==palabraBuscar:
            array[i]=palabraNueva
    return array

print(ejercicio7(" hola  que tal   ", "que", "si"))