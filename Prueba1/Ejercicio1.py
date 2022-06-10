'''
Created on 7 Jun 2022

@author: estudiante
'''


edad=int(input("Introduce tu edad: "))
while edad<0:
    print("La edad no puede ser menor de 0")
    edad=int(input("Introduce tu edad de forma correcta: "))

covid=input("Has pasado el covid? S/N: ")
while covid!="S" and covid!="N":
    print("Introduce S o N")
    covid=input("Has pasado el covid? S/N: ")

vacuna=input("Que vacuna has recibido? P para Pfizer, M para Moderna, A para Astrazeneca: ")
while vacuna!="P" and vacuna!="M" and vacuna!="A":
    print("Introduce P, M o A")
    vacuna=input("Que vacuna has recibido? P para Pfizer, M para Moderna, A para Astrazeneca: ")

if vacuna=="A":
    cadena="Debe volver a vacunarse"
    
elif vacuna=="M":
    if edad>60 and covid=="N":
        cadena="Debe volver a vacunarse"
    else:
        cadena="No debe volver a vacunarse"

else:
    if covid=="N":
        cadena="Debe volver a vacunarse"
    elif covid=="S" and edad>70:
        cadena="Debe volver a vacunarse"
    else:
        cadena="No debe volver a vacunarse"

print(cadena)



