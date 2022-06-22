'''
Created on 17 Jun 2022

@author: estudiante
'''
def login(nombre, contrasena):
    resultado=False
    if nombre=="usuario1" and contrasena=="asdasd":
        resultado=True
    return resultado

salir=False
contador=0
while salir==False and contador<3:
    contador+=1
    nombre=input("Introduce un nombre: ")
    contrasena=input("Introduce una contrasena: ")
    if(login(nombre, contrasena)):
        salir=True
        print("Login correcto")
    else:
        print("Login incorrecto, intente de nuevo")