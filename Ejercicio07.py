# Programa que lea números enteros por teclado y para cada número
# introducido indique si es positivo o negativo y si es par o impar.
# Se deben realizar tres versiones del programa:
# En la primera versión se utilizará un bucle while.
# La lectura de números finalizará cuando se introduzca un cero.
# En la tercera versión también se utilizará un bucle do .. while pero
# en este caso la lectura de números finaliza cuando se responda "N" ó "n"
# a la pregunta "¿Desea introducir más números? (S/N):"

import os
# limpiar la pantalla
os.system('cls')
print("------------------------------------------------------------")
print("-            Identificación de Números Enteros             -")
print("------------------------------------------------------------")
bucle = True
while (bucle == True):
    numero = int(input("Introduce un número entero: "))
    if (numero == 0):
        print("El número introducido es cero (0).")
    else:
        # Ver si es par o impar
        if ((numero % 2) == 0):
            tipo = "par"
        else:
            tipo = "impar"
        # Ver si es positivo o negativo
        if (numero > 0):
            posi = "positivo"
        else:
            posi = "negativo"
        # Mostramos datos
        print("El número", numero, "es " + tipo + " y " + posi + ".")

    # para continuar o no
    opcion = ""
    while (opcion != "n" and opcion != "N" and opcion != "s" and opcion != "S"):
        opcion = input("¿Desea continuar introduciendo números? (S/N): ")
        if (opcion == "n" or opcion == "N"):
            bucle = False
        elif (opcion == "s" or opcion == "S"):
            bucle = True
print("bye!")
