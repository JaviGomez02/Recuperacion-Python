'''
Created on 3 Jun 2022

@author: estudiante
'''

def eliminarComentarios(cadena):
    resultado=""
    encontrado=False
    for i in range(0, len(cadena)):
        if i!=len(cadena)-1:
            if cadena[i]=="/" and cadena[i+1]=="*":
                encontrado=True
            
            if encontrado==False and cadena[i]!="/" and cadena[i]!="*":
                resultado=resultado+cadena[i]
    
            if cadena[i]=="*" and cadena[i+1]=="/":
                encontrado=False
        elif cadena[i]!="*" and cadena[i]!="/":
            resultado=resultado+cadena[i]
    
    return resultado

print(eliminarComentarios("aaaa/*eee*/ee/*uuu*/ii"))