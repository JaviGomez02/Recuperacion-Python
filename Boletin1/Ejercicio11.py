'''
Created on 3 Jun 2022

@author: estudiante
'''
segundos=int(input("Introduce el numero de segundos: "))
minutos=0
horas=0

while segundos>=60:
    minutos+=1
    segundos-=60

while minutos>=60:
    horas+=1
    minutos-=60
    
print(str(horas)+" horas "+str(minutos)+" minutos y "+str(segundos)+" segundos")




