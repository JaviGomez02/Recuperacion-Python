'''
Created on 20 Jun 2022

@author: estudiante
'''

def palabraEscondida(cadena, cadenaBuscar):
    resultado=False
    contador=0
    aux=""
    for i in range(len(cadenaBuscar)):
        salir=False
        caracter=cadenaBuscar[i]
        while(contador<len(cadena) and salir==False):
            if cadena[contador]==caracter:
                salir=True
                aux+=cadena[contador]
            contador+=1   
        if cadenaBuscar==aux:
            resultado=True
    return resultado

print(palabraEscondida("shybaoxlna", "hola"))
            
            
    