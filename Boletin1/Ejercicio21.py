'''
Created on 6 Jun 2022

@author: estudiante
'''

vector=[]
salir=False
while (len(vector)<10 and salir==False):
    numero=int(input("Introduce un numero: "))
    if numero>=0:   
        vector.append(numero)
    else:
        salir=True


print(vector)