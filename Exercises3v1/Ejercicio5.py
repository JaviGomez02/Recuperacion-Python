'''
Created on 13 Jun 2022

@author: estudiante
'''

def myPower(num, potencia):
    resultado=num
    if potencia<0:
        resultado=-1
    elif potencia==0:
        resultado=1
    else:
        for i in range(1,potencia):
            resultado=resultado*num
    return resultado

print(myPower(2, 3))
        
    
    

