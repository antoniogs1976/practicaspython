# Programa que lea un carácter por teclado y compruebe si es una letra mayúscula
import os
bucle = True
while (bucle == True):
    # limpiar la pantalla
    os.system('cls')
    print("------------------------------------------------------------")
    print("-   L E T R A   M A Y Ú S C U L A   O   M I N Ú S C U L A  -")
    print("------------------------------------------------------------")
    letra = input("Por favor, introduce una letra: ")
    # usando islower...
    if letra.islower() == True:
        print("la letra es minúscula.")
    else:
        print("la letra es mayúscula.")
    
    # para continuar o no
    opcion=input("¿Desea continuar introduciendo números? (S/N): ")
    if (opcion == "n" or opcion == "N"):
        bucle = False
    else:
        bucle = True