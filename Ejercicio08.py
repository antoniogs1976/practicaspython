# Programa que lea por teclado 10 números enteros y los guarde en un array.
# A continuación calcula y muestra por separado la media de los valores
# positivos y la de los valores negativos.
import os
bucle = True
while (bucle == True):
    numeros = [0,0,0,0,0,0,0,0,0,0]
    total = 0
    positivos = 0
    negativos = 0
    mediaPositivos = 0
    mediaNegativos = 0
    os.system('cls')
    print("------------------------------------------------------------")
    print("-     Array 10 números y media de positivos y negativos    -")
    print("------------------------------------------------------------")
    for x in range(0,10):
        contador = x + 1
        print("Número: ", contador)
        numeros[x]=int(input("Introduce su valor: "))

    # Recorrer el array actualizando las medias y el total según sea el valor del elemento del array
    for x in range(0, len(numeros)):
        total += numeros[x]
        if (numeros[x] > 0):
            mediaPositivos += numeros[x]
            positivos += 1
        else:
            mediaNegativos += numeros[x]
            negativos += 1

    # Ahora toca calcular las medias reales dividiendo por el número de elementos
    if (positivos > 0):
        mediaPositivos = mediaPositivos / positivos
    
    if (negativos > 0):
        mediaNegativos = mediaNegativos / negativos
    
    # Mostramos los resultados
    print("Media de los números positivos: ", mediaPositivos)
    print("Media de los números negativos: ", mediaNegativos)
    print("Suma total de los números: ", total)

    # para continuar o no
    opcion = input("¿Desea continuar introduciendo números? (S/N): ")
    if (opcion == "n" or opcion == "N"):
        bucle = False
    else:
        bucle = True
