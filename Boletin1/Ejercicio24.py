'''
Created on 6 Jun 2022

@author: estudiante
'''
vector1=[]
vector2=[]
vector3=[]
for i in range(0, 5):
    vector1.append(int(input("Introduce numeros para el vector1: ")))
    
for i in range(0, 5):
    vector2.append(int(input("Introduce numeros para el vector2: ")))
    
for i in range(0, 5):
    vector3.append(vector1[i]+vector2[i])

print("Vector 1: "+str(vector1))
print("Vector 2: "+str(vector2))
print("Vector 3: "+str(vector3))

    
    
    