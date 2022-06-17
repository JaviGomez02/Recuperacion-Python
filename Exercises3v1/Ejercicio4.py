'''
Created on 10 Jun 2022

@author: estudiante
'''
def dayOfWeek(dia, mes, anno):
    a=(14-mes)/12
    y=anno-a
    m=mes+12*a-2
    d=(dia+y+y/4-y/100+y/400+(31*m)/12)%7
    return round(d, 0)

print(dayOfWeek(13, 6, 2022))
    
    
    