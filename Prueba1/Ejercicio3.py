'''
Created on 7 Jun 2022

@author: estudiante
'''

numeros=int(input("Cuantos numeros quieres introducir para generar la clave? "))
clave=0
for i in range(0, numeros):
    num=int(input("Introduce un numero: "))
    if num<0:
        num=-num
    resto=num%5
    if resto%2!=0:
        clave=clave+resto

print("La clave es: "+str(clave))