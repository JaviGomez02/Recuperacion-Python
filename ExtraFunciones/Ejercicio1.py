'''
Created on 17 Jun 2022

@author: estudiante
'''
def esMultiplo(num1, num2):
    resultado=False
    if num1%num2==0:
        resultado=True
    return resultado

print(esMultiplo(45, 5))