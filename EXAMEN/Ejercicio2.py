'''
Created on 22 Jun 2022

@author: estudiante
'''


notasAprobados=[]
notaMayor=0
suma=0
alumnos=int(input("¿Cuantos alumnos tiene la clase? "))

while alumnos<0:
    alumnos=int(input("No puede haber menos de 0 alumnos, vuelve a introducir el numero de alumnos: "))

for i in range(0, alumnos):
    nota=int(input("Introduce la nota del alumno "+str(i+1)+": "))
    while nota<0 or nota>10:
        print("Nota incorrecta")
        nota=int(input("Introduce la nota del alumno "+str(i+1)+": "))
    if nota>=5:
        notasAprobados.append(nota)
    if nota>notaMayor:
        notaMayor=nota
    
print("El alumno con mejor nota tiene un "+str(notaMayor))

if len(notasAprobados)==0:
    print("No hay aprobados. No puede calcularse la media")
else:
    for i in range(len(notasAprobados)):
        suma+=notasAprobados[i]
    print("La nota media de los aprobados es "+str(round(suma/len(notasAprobados),2)))
    
    
    
    
    
    
    
    