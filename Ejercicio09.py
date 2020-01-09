# Programa que crea un array de 20 elementos llamado Pares y guarde los 20
# primeros números pares. Mostrar por pantalla el contenido del array creado
import os
os.system('cls')
pares = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print("--------------------------------------------------------------------------")
print("-                Array con los 20 primeros números pares                 -")
print("--------------------------------------------------------------------------")
# rellenar el array con los datos
maximo = len(pares)
for x in range(0, maximo):
    pares[x] = (x + 1) * 2
# mostrar datos
for x in range(0, maximo):
    print(pares[x])