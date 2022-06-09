'''
Created on 31 May 2022

@author: estudiante
'''
num=-1
while num<0 or num>4:
    num=int(input("Cuantos decimales quieres? Maximo 4 "))
    
pi = 4*(1-1/3+1/5-1/7)

cadena=str(pi);
cadenaNueva=""
for i in range(0, num+2):
    cadenaNueva=cadenaNueva+cadena[i]
print(cadenaNueva)