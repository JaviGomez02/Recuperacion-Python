'''
Created on 30 May 2022

@author: estudiante
'''
import math
num = int(input("Introduce un numero: "))
raiz = math.sqrt(num)
raizEntero = int(raiz)
if raiz - raizEntero == 0:
    print("El numero introducido es el cuadrado de un numero entero")
else:
    print("El numero no es un cuadrado de un numero entero")
