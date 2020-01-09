# Programa que pida que se introduzcan dos números enteros por teclado
# y muestre los números que van desde el menor hasta el mayor de los
# números introducidos. Los dos números introducidos deben ser distintos.
# Si son iguales se mostrará un mensaje indicandolo y se vuelven a introducir.
import os
bucle = True
while (bucle == True):
    # limpiar la pantalla
    os.system('cls')
    num1 = 0
    num2 = 0
    print("------------------------------------------------------------")
    print("-         N Ú M E R O S   E N T R E   N Ú M E R O S        -")
    print("------------------------------------------------------------")
    while (num1 == num2):
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        if (num1 == num2):
            print("* ERROR * Los números deben ser diferentes.")

    # Comprobar cual es mayor y cual es menor

    if (num1 < num2):
        menor = num1
        mayor = num2 + 1
    else:
        menor = num2
        mayor = num1 + 1

    # poner las cosas
    for x in range(menor, mayor):
        print(x)

    # para continuar o no
    opcion = input("¿Desea continuar introduciendo números? (S/N): ")
    if (opcion == "n" or opcion == "N"):
        bucle = False
    else:
        bucle = True
