'''
Created on 6 Jun 2022

@author: estudiante
'''
vectorNotas=[]
notaAlta=0
notaBaja=999
suma=0
for i in range (0, 5):
    vectorNotas.append(int(input("Introduce una nota: ")))
for i in range (0, len(vectorNotas)):
    nota=vectorNotas[i]
    if nota>notaAlta:
        notaAlta=nota
    if nota<notaBaja:
        notaBaja=nota
    suma=suma+nota

print("Las notas son: "+str(vectorNotas))
print("La nota mas alta es: "+str(notaAlta)+", la nota mas baja es: "+str(notaBaja)+", y la media es: "+str(suma/len(vectorNotas)))