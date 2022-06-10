'''
Created on 10 Jun 2022

@author: estudiante
'''
def pasarMayuscula(cadena):
    resultado=""
    for i in range(0, len(cadena)):
        ascii=ord(cadena[i])
        if ascii>=97:
            ascii=ascii-32
        resultado=resultado+chr(ascii)
    
    return resultado

boton=""
melodia=""
while boton!="P":
    boton=pasarMayuscula(input("Introduce un boton: A, B o P: "))
    
    if boton!="P":
        if boton=="A":
            if melodia!="A1":
                melodia="A1"
            else:
                melodia="A2"
        elif boton=="B":
            if melodia!="B1":
                melodia="B1"
            else:
                melodia="B2"
        print("Esta sonando la melodia "+melodia)
    else:
        print("Apagando...")

