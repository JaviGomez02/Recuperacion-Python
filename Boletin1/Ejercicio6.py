'''
Created on 31 May 2022

@author: estudiante
'''
num=int(input("Introduce un numero: "))
cadena=""
num2=num
for i in range(2,num+1):
    while num%i==0:
        cadena=cadena+str(i)+" "
        num=num/i
    
print(cadena)







