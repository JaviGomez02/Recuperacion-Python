'''
Created on 31 May 2022

@author: estudiante
'''


num=int(input("Introduce un numero para pasarlo a binario: "))
cadena=""
cadenaFinal=""

while num>=1:
    resto=int(num%2)
    if num%2==0:
        num=num/2
    else:
        num=(num-1)/2
    cadena=cadena+str(resto)

for i in range (len(cadena)-1,-1,-1):
    cadenaFinal=cadenaFinal+cadena[i]
    
    

print(cadenaFinal)

















