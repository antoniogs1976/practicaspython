# Programa que lea por teclado tres números enteros H, M, S correspondientes
# a hora, minutos y segundos respectivamente, y comprueba si la hora que
# indican es una hora válida.
import os
bucle = True
while (bucle == True):
    # limpiar la pantalla
    os.system('cls')
    print("------------------------------------------------------------")
    print("-  Horas, Minutos y Segundos de una hora válida (o no...)  -")
    print("------------------------------------------------------------")
    HH = int(input("Por favor, introduce las horas (0-23): "))
    MM = int(input("Por favor, introduce los minutos (0-59): "))
    SS = int(input("Por favor, introduce los segundos (0-59): "))
    # comprobaciones:

    print("Has introducido estos datos: ", HH, ":", MM, ":", SS)
    if (HH < 0) or (HH > 23):
        print("- las horas(" + HH + ") no son válidas.")
    else:
        if (MM < 0) or (MM > 59):
            print("- los minutos (" + MM + ") no son válidos.")
        else:
            if (SS < 0) or (SS > 59):
                print("- los segundos (" + SS + ") no son válidos.")
            else:
                print("Los datos introducidos corresponden a una hora correcta.")
    
    # para continuar o no
    opcion = ""
    while (opcion != "n" and opcion != "N" and opcion != "s" and opcion != "S"):
        opcion = input("¿Desea continuar introduciendo números? (S/N): ")
        if (opcion == "n" or opcion == "N"):
            bucle = False
        elif (opcion == "s" or opcion == "S"):
            bucle = True
print("bye!")
