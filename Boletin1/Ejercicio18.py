'''
Created on 3 Jun 2022

@author: estudiante
'''
import random

vector_numeros=[]
for i in range (0,10):
    vector_numeros.append(random.randint(0,10))

for i in range (0,len(vector_numeros)):
    cuadrado=vector_numeros[i]*vector_numeros[i]
    cubo=vector_numeros[i]*vector_numeros[i]*vector_numeros[i]
    print("Valor: "+str(vector_numeros[i])+". Su cuadrado es: "+str(cuadrado)+" Y su cubo es: "+str(cubo))


