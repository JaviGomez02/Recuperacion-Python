'''
Created on 31 May 2022

@author: estudiante
'''
numEntradas = int(input("Introduce el numero de entradas: "))
dia = input("Introduce el dia (L,M,X,J,V,S,D): ")
tarjeta = input("Tienes tarjeta CineJacaranda? (S/N): ")
precio = 0
if dia == "X":
    precio = numEntradas * 5
elif dia == "J":
    while numEntradas > 1:
        precio = precio + 11
        numEntradas = numEntradas - 2
    if numEntradas == 1:
        precio = precio + 8
else:
    precio = numEntradas * 8        

if tarjeta == "S":
    precio = precio - precio * 0.10

print("El precio de su compra es " + str(precio) + " euros")

