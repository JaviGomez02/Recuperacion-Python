'''
Created on 13 Jun 2022

@author: estudiante
'''

def friend(num1, num2):
    resultado=False
    divisores1=[]
    divisores2=[]
    suma1=0
    suma2=0
    for i in range(1, num1-1):
        if num1%i==0:
            divisores1.append(i)
    for i in range(1, num2-1):
        if num2%i==0:
            divisores2.append(i)
    for i in range(0, len(divisores1)):
        suma1=suma1+divisores1[i]
    for i in range(0, len(divisores2)):
        suma2=suma2+divisores2[i]
    
    if suma1==num2 and suma2==num1:
        resultado=True
    return resultado


print(friend(220, 284))