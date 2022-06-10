'''
Created on 10 Jun 2022

@author: estudiante
'''

lista=[]
num=1
while num!=0:
    num=int(input("Introduce numeros: "))
    if num!=0:
        lista.append(num)
print(lista)

listaNueva=[]
for i in range(0, len(lista)-1):
    if lista[i]>lista[i+1]:
        num=1
    elif lista[i]==lista[i+1]:
        num=0
    else:
        num=-1
    listaNueva.append(num)

print(listaNueva)