'''
Created on 7 Jun 2022

@author: estudiante
'''
mes=999
contadorMenores=0
contadorMediaEdad=0
contadorMayores=0

while mes>0:
    mes=int(input("Introduce el mes de nacimiento. Para terminar el programa introduce -1: "))
    while mes>12:
        mes=int(input("Introduce un mes correcto: "))
    if mes>0:
        anno=int(input("Introduce el anno de nacimiento: "))
        while anno>2022:
            print("Introduce un anno correcto")
            anno=int(input("Introduce el anno de nacimiento: "))
        edad=2022-anno
        if mes>=6:
            edad-=1
        
        if edad<30:
            contadorMenores+=1
        elif edad>=50:
            contadorMayores+=1
        else:
            contadorMediaEdad+=1
    else:
        print("Hay "+str(contadorMenores)+" pacientes con menos de 30 annos")
        print("Hay "+str(contadorMediaEdad)+" pacientes entre 31 y 49 annos")
        print("Hay "+str(contadorMayores)+" pacientes con 50 annos o mas")