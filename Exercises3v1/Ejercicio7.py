'''
Created on 13 Jun 2022

@author: estudiante
'''

def isPrime(num):
    resultado=1
    if num<=0:
        resultado=-1
    else:
        for i in range(2, num-1):
            if num%i==0:
                resultado=0
    return resultado

print(isPrime(7))




