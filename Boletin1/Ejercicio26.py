'''
Created on 6 Jun 2022

@author: estudiante
'''
vectorMaxima=[]
vectorMinima=[]
for i in range(0, 5):
    tempMax=int(input("Introduce la temperatura maxima del dia "+str(i+1)+": "))
    tempMin=int(input("Introduce la temperatura minima del dia "+str(i+1)+": "))
    vectorMaxima.append(tempMax)
    vectorMinima.append(tempMin)
    
#La temperatura media de cada día
for i in range (0, 5):
    media=int((vectorMaxima[i]+vectorMinima[i])/2)
    print("La temperatura media del dia "+str(i+1)+" es de "+str(media)+" grados.")
    

#Los días con menos temperatura
menorTemp=9999999
for i in range (0, 5):
    if vectorMinima[i]<menorTemp:
        menorTemp=vectorMinima[i]
        dia=i+1
print("El dia con menor temperatura es el dia "+str(dia)+" con una temperatura de "+str(menorTemp)+" grados.")

#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
# si no existe ningún día se muestra un mensaje de información.

temp=int(input("Introduce una temperatura: "))
dias=[]
existe=False
for i in range (0, 5):
    if vectorMaxima[i]==temp:
        dias.append(i+1)
        existe=True


if existe==True:
    print("Los dias que coinciden con la temperatura introducida son: "+str(dias))
else:
    print("No se encontro ningun dia que coincida con esa temperatura")


