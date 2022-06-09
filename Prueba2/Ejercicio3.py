'''
Created on 9 Jun 2022

@author: estudiante
'''
def ejercicio3(texto, longitud):
    palabra=""
    resultado=""
    for i in range(0, len(texto)):
        if texto[i]!=" ":
            palabra=palabra+texto[i]
        else:
            if len(palabra)<longitud:
                resultado=resultado+palabra+" "
            else:
                palabraNueva=""
                for i in range (0, longitud):
                    palabraNueva=palabraNueva+palabra[i]
                palabraNueva=palabraNueva+"@"+" "
                resultado=resultado+palabraNueva
                
            palabra=""
    if palabra!="":
        if len(palabra)<longitud:
                resultado=resultado+palabra+" "
        else:
            palabraNueva=""
            for i in range (0, longitud):
                palabraNueva=palabraNueva+palabra[i]
            palabraNueva=palabraNueva+"@"+" "
            resultado=resultado+palabraNueva
                
    return resultado


print(ejercicio3("hola que hace mi socio",3))