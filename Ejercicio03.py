# Programa que lea por teclado tres números enteros y calcule el mayor de los tres.
import os
bucle = True
# limpiar la pantalla
os.system('cls')
print("------------------------------------------------------------")
print("-        M A Y O R   D E   T R E S   N Ú M E R O S         -")
print("------------------------------------------------------------")
num1 = input("Por favor, teclea el primer número: ")
num2 = input("Por favor, teclea el segundo número: ")
num3 = input("Por favor, teclea el tercer número: ")
if (num1 > num2 and num1 > num3):
    print("El primer número (" + num1 + ") es el mayor de los tres.")
else:
    if (num2 > num1 and num2 > num3):
        print("El segundo número (" + num2 + ") es el mayor de los tres.")
    else:
        print("El tercer número (" + num3 + ") es el mayor de los tres.")