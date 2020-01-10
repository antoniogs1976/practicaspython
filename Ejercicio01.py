# Programa que lea un número entero por teclado y calcule si es par o impar.
import os
bucle = True
while (bucle == True):
    # limpiar la pantalla
    os.system('cls')
    print("------------------------------------------------------------")
    print("-                 P A R    O    I M P A R                  -")
    print("------------------------------------------------------------")
    numero = input("Por favor, introduce un número: ")
    if ((int(numero) % 2) == 0):
        print("El numero "+ numero +" es par.")
    else:
        print("El numero "+ numero +" es impar.")

    # para continuar o no
    opcion = ""
    while (opcion != "n" and opcion != "N" and opcion != "s" and opcion != "S"):
        opcion = input("¿Desea continuar introduciendo números? (S/N): ")
        if (opcion == "n" or opcion == "N"):
            bucle = False
        elif (opcion == "s" or opcion == "S"):
            bucle = True
print("bye!")
