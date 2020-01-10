# Programa que guarda en un array 10 números enteros que se leen por teclado.
# A continuación se recorre el array y calcula cuántos números son positivos,
# cuántos negativos y cuántos ceros.

import os
bucle = True
while (bucle == True):
    # inicializar variables
    numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ceros = 0
    positivos = 0
    negativos = 0
    # limpiar la pantalla
    os.system('cls')
    print("------------------------------------------------------------")
    print("-  Array 10 números y contar positivos, negativos y ceros  -")
    print("------------------------------------------------------------")
    for x in range(0, 10):
        if (x < 10):
            texto = "0"+str(x+1)+" - Introduce el valor: "
        else:
            texto = str(x+1)+" - Introduce el valor: "
        numeros[x] = int(input(texto))

    # Recorrer el array actualizando los datos
    for x in range(0, 10):
        if (numeros[x] == 0):
            ceros += 1
        elif (numeros[x] > 0):
            positivos += 1
        else:
            negativos += 1
    
    # Mostramos los resultados
    print("Has introducido", positivos, "números positivos.")
    print("Has introducido", negativos, "números negativos.")
    print("Has introducido", ceros, "ceros.")

    # para continuar o no
    opcion = input("¿Desea continuar introduciendo números? (S/N): ")
    if (opcion == "n" or opcion == "N"):
        bucle = False
    else:
        bucle = True