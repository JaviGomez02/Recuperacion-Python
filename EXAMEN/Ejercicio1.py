'''
Created on 22 Jun 2022

@author: estudiante
'''

AUMENTO_5_ANNOS=5
AUMENTO_10_ANNOS=7
AUMENTO_MAYOR=10.2

numHoras=int(input("Introduce el numero de horas mensuales trabajadas: "))
while(numHoras<0):
    print("Las horas trabajadas no pueden ser negativas")
    numHoras=int(input("Introduce el numero de horas mensuales trabajadas: "))

categoria=input("Introduce la categoria. APRENDIZ, MAESTRO o SUPER MAESTRO: ")
while(categoria!="APRENDIZ" and categoria!="MAESTRO" and categoria!="SUPER MAESTRO"):
    print("Categoria incorrecta")
    categoria=input("Introduce la categoria. APRENDIZ, MAESTRO o SUPER MAESTRO: ")

numAnnos=int(input("Introduce el numero de annos trabajados: "))
while(numAnnos<0 or numAnnos>50):
    print("Numero de annos incorrectos")
    numAnnos=int(input("Introduce el numero de annos trabajados: "))

if categoria=="APRENDIZ":
    sueldo=30*numHoras
elif categoria=="MAESTRO":
    sueldo=40*numHoras
else:
    sueldo=50*numHoras


if numAnnos<5:
    aumento=AUMENTO_5_ANNOS*sueldo/100
    sueldo+=aumento
elif numAnnos<10:
    aumento=AUMENTO_10_ANNOS*sueldo/100
    sueldo+=aumento
else:
    aumento=AUMENTO_MAYOR*sueldo/100
    sueldo+=aumento
    
    
print("Su sueldo es de "+str(sueldo)+" euros")












