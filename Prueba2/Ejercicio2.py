'''
Created on 7 Jun 2022

@author: estudiante
'''

mesas=[0,0,0,0,0,0,0,0,0,0]

clientes=0

while clientes!=-1:
    salir=False
    i=0
    clientes=int(input("Cuantos clientes sois? "));
    while clientes>4:
        clientes=int(input("No podeis ser mas de 4. Cuantos sois? "));
    while salir==False:
        if mesas[i]+clientes<=4:
            mesas[i]=mesas[i]+clientes
            print("Os podeis sentar en la mesa "+str(i))
            salir=True
        i=i+1
    print(mesas)