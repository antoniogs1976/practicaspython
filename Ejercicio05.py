# Programa que lea una variable entera mes y compruebe si el valor corresponde
# a un mes de 30 días, de 31 o de 28. Supondremos que febrero tiene 28 días.
# Se mostrará además el nombre del mes. Se debe comprobar que el valor introducido
# esté comprendido entre 1 y 12.
import os
bucle = True
while (bucle == True):
    # limpiar la pantalla
    os.system('cls')
    mes = 0
    print("------------------------------------------------------------")
    print("-    D Í A S   Y   N O M B R E   D E   L O S   M E S E S   -")
    print("------------------------------------------------------------")
    while (mes < 1 or mes > 12):
        mes = int(input("Introduce el número del mes (1-12): "))
        if (mes < 1 or mes > 12):
            print("Mes no válido. Introduce otro válido (1 a 12).")
    # mes válido, así que hacemos cosas...
    if (mes == 1):
        meses = "Enero"
        dias = 31
    elif (mes == 2):
        meses = "Febrero"
        dias = 28
    elif (mes == 3):
        meses = "Marzo"
        dias = 31
    elif (mes == 4):
        meses = "Abril"
        dias = 30
    elif (mes == 5):
        meses = "Mayo"
        dias = 31
    elif (mes == 6):
        meses = "Junio"
        dias = 30
    elif (mes == 7):
        meses = "Julio"
        dias = 31
    elif (mes == 8):
        meses = "Agosto"
        dias = 31
    elif (mes == 9):
        meses = "Septiembre"
        dias = 30
    elif (mes == 10):
        meses = "Octubre"
        dias = 31
    elif (mes == 11):
        meses = "Noviembre"
        dias = 30
    elif (mes == 12):
        meses = "Diciembre"
        dias = 31
    # Mostramos el resultado
    print("El mes", mes, "corresponde a " + meses + " y tiene", dias, "días.")

    # para continuar o no
    opcion = input("¿Desea continuar introduciendo números? (S/N): ")
    if (opcion == "n" or opcion == "N"):
        bucle = False
    else:
        bucle = True
