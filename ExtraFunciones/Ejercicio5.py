'''
Created on 17 Jun 2022

@author: estudiante
'''

def calcularMCD(num1, num2):
    resultado=0
    salir=False
    while salir==False:
        if num1%num2==0:
            resultado=num2
            salir=True
        else:
            num2=num1%num2
    return resultado


print(calcularMCD(24,20))

