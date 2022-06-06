'''
Created on 6 Jun 2022

@author: estudiante
'''
mes=int(input("Introduce un mes: "))
vectorDias=[31,28,31,30,31,30,31,31,30,31,30,31]
vectorMeses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
print("El mes de "+str(vectorMeses[mes-1])+" tiene "+str(vectorDias[mes-1])+" dias")