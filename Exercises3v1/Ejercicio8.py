'''
Created on 13 Jun 2022

@author: estudiante
'''

def secondOrder(a, b, c):
    raiz=4*a*c-b**2
    if raiz<0:
        resultado=0
    elif raiz==0:
        resultado=1
    elif raiz>0:
        resultado=2
    return resultado

print(secondOrder(2, 1, 4))
    
    
    
    


