'''
Created on 6 Jun 2022

@author: estudiante
'''

salir=False
alumnosAdultos=[]
edadAlumnos=[]
alumnosViejos=[]
edadMayor=0

while salir==False:
    nombre=input("Introduce el nombre del alumno: ")
    if nombre=="*":
        salir=True
    else:
        edad=int(input("Introduce la edad del alumno: "))
        if edad>=18:
            alumnosAdultos.append(nombre)
            edadAlumnos.append(edad)
        if edad>edadMayor:
            edadMayor=edad

for i in range(0, len(edadAlumnos)):
    if edadAlumnos[i]==edadMayor:
        alumnosViejos.append(alumnosAdultos[i])
    
    
print("Los alumnos mayores de edad son: "+str(alumnosAdultos))
print("Los alumnos mas mayores son: "+str(alumnosViejos)+" con "+str(edadMayor)+" annos")