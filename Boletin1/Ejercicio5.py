'''
Created on 31 May 2022

@author: estudiante
'''
num=-1
while num<0 or num>4:
    num=int(input("Cuantos decimales quieres? Maximo 4 "))
    
pi = "3.1415"
print(pi)
cadena=""

for i in range(0, num+2):
    cadena=cadena+pi[i]

print(cadena)