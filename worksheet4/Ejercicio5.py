'''
Created on 20 Jun 2022

@author: estudiante
'''
def palindromo(cadena):
    resultado=False
    cadenaReves=""
    for i in range(len(cadena)-1, -1, -1):
        cadenaReves+=cadena[i]
    
    if cadena==cadenaReves:
        resultado=True
    
    return resultado

print(palindromo("anilina"))