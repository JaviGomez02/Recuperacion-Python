'''
Created on 10 Jun 2022

@author: estudiante
'''
def leapYear(numero):
    if numero%400==0:
        resultado=1
    else:
        if numero%4==0 and numero%100!=0:
            resultado=1
        else:
            resultado=-1
    return resultado

def daysInMonth(anno, mes):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    if anno<0 or mes<0 or mes>12:
        dia=-1
    elif leapYear(anno)==1 and mes==2:
        dia=29
    else:
        dia=dias[mes-1]
    return dia

print(daysInMonth(1998, 4))

print(daysInMonth(2000, 2))