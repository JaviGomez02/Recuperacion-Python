'''
Created on 6 Jun 2022

@author: estudiante
'''
import random


vector=[]
for i in range(0, 10):
    vector.append(random.randint(0,50))
print(vector)

print(sorted(vector))