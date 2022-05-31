'''
Created on 30 May 2022

@author: estudiante
'''

num = 0
suma = 0
while num >= 0:
    num = int(input("Introduce un numero: "))
    if num >= 0:
        for i in range (1, num + 1):
            suma = suma + i
print(suma)
    
