'''
Created on 17 Jun 2022

@author: estudiante
'''
def calcularMedia(max, min):
    return (max+min)/2

num=int(input("Cuantos dias quieres introducir? "))

for i in range(0, num):
    tMax=int(input("Introduce la temperatura maxima: "))
    tMin=int(input("Introduce la temperatura minima: "))
    print("La temperatura media es de "+str(calcularMedia(tMax, tMin))+" grados")
    
    
    
    
    
    