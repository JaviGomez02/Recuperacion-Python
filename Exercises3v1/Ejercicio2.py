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

print(leapYear(2020))
    