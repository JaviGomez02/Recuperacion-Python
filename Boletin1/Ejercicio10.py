'''
Created on 2 Jun 2022

@author: estudiante
'''

def codificar(cadena, clave):
    resultado=""
    for i in range(0, len(cadena)):
        numero=int(cadena[i])
        for j in range(0, len(clave)):
            if numero==j:
                resultado=resultado+clave[j]
    
    return resultado

def decodificar(cadena, clave):
    resultado=""
    for i in range(0, len(cadena)):
        numero=int(cadena[i])
        for j in range(0, len(clave)):
            if numero==int(clave[j]):
                resultado=resultado+str(j)
    
    
    
    
    return resultado

print(codificar("4614", "3651829470"))
print(decodificar("8968", "3651829470"))