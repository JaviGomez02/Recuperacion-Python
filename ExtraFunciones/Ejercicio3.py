'''
Created on 17 Jun 2022

@author: estudiante
'''
from cmath import pi

def calcularArea(radio):
    return pi*(radio**2)

def calcularPerimetro(radio):
    return 2*pi*radio

print(calcularArea(5))

print(calcularPerimetro(5))