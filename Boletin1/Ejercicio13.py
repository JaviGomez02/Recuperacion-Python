'''
Created on 3 Jun 2022

@author: estudiante
'''
def pasarMayuscula(cadena):
    resultado=""
    for i in range(0, len(cadena)):
        ascii=ord(cadena[i])
        if ascii>=97:
            ascii=ascii-32
        resultado=resultado+chr(ascii)
    
    return resultado

def esPalindroma(cadena):
    resultado=False
    cadena1=""
    cadena2=""
    for i in range(0,len(cadena)):
        cadena1=cadena1+cadena[i]
    for i in range(len(cadena)-1,-1,-1):
        cadena2=cadena2+cadena[i]
    if pasarMayuscula(cadena1)==pasarMayuscula(cadena2):
        resultado=True
    
    
    return resultado
    
    
    
print(esPalindroma("holalala"))
print(esPalindroma("aaiiaa"))







