'''
Created on 31 May 2022

@author: estudiante
'''
num = 0
minimo = 9999999999
maximo = 0
total = 0
contador = 0
while num >= 0:
    num = int(input("Introduce un numero: "))
    if num >= 0:
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num
        total = total + num
        contador = contador + 1
print(minimo)
print(maximo)
print(total / contador)

