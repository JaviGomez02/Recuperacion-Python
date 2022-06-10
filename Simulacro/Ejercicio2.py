'''
Created on 10 Jun 2022

@author: estudiante
'''
altura=1
peso=1
edad=1

while altura>0 and peso>0 and edad>0:

    altura=float(input("Introduce tu altura: "))
    peso=int(input("Introduce tu peso: "))
    edad=int(input("Introduce tu edad: "))
    
    if altura>0 and peso>0 and edad>0:

        imc=peso/(altura**2)
        print("Su IMC es de: "+ str(imc))

        if imc<18.5:
            cadena="Peso insuficiente"
        elif imc<24.9:
            cadena="Normopeso"
        elif imc<29.9:
            cadena="Sobrepeso"
        elif imc<39.9:
            cadena="Obesidad"
        else:
            cadena="Obesidad mórbida"
        
        print("Para un peso de "+str(peso)+" kilogramos y una talla de "+str(altura)+" metros, su IMC es: "+str(imc))
    
        if imc>25 and edad>45:
            print("Dada su edad e IMC es recomendable que cuide su salud cardiovascular")
        elif imc>30:
            print("Dado su imc es muy recomendable que cuide su salud cardiovascular")
    else:
        print("Saliendo...")

