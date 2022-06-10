'''
Created on 10 Jun 2022

@author: estudiante
'''
def factorial(numero):
    if numero<0:
        resultado=-1
    else:
        contador=1
        resultado=1
        for i in range(0,numero):
            resultado=resultado*contador
            contador+=1
    return resultado

print(factorial(5))