'''
Created on 6 Jun 2022

@author: estudiante
'''

vector=[]
vector_inverso=[]
for i in range (0, 5):
    vector.append(input("Introduce una cadena: "))

for i in range(len(vector)-1,-1,-1):
    vector_inverso.append(vector[i])
    
print(vector_inverso)