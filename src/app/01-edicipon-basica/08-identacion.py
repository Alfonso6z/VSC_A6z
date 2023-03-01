"""
*    Objetivo.
*        Corregir la identación
?    shortcuts:
?        Tab - ->
?        Shift + tab <-
&    selecciona las lineas que deseas identar
"""
n = 10
m = 9
for i in range(n):
            for j in range(m):
        if(i%2==0):
    print(f"{i}*{j} = {i*j}")
    else:
        print(f"{i}**2 = {i**2}")
    print("termina programa")