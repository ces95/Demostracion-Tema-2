"""
Realizado por:

Cesar A. Diaz - 1075235
Salma Marmol - 108

"""

# Librerias
import os
import sys
import numpy as np




#FUNCIONES


#INICIO DEL MENU DEL PROGRAMA
ans = ''
while ans :
    print(
        """
        Menu de Inicio
        --- Seleccione una de las siguiente opciones con los numeros ---
        [1] Encriptar
        [2] Desencriptar
        [3] Salir

        """)

    ans = input("Que desea hacer? ")

    if ans=="1":
        os.system('cls')
        print(
            """
            Menu de Encriptado
            --- Seleccione una de las siguiente opciones con los numeros ---
            [1] Encriptar por Algoritmo Simetrico
            [2] Encriptar por Algoritmo Asimetrico
            [3] Encriptar por Algoritmo basado en Matriz
            [4] Retornar

            """)
        s = input("Que desea hacer? ")

        if s=='1':
            os.system('cls')
            print("Encriptar por Algoritmo Simetrico")
            os.system('pause')

        elif s=='2':
            os.system('cls')
            print("Encriptar por Algoritmo Asimetrico")
            os.system('pause')


        elif s=='3':
            os.system('cls')
            print("Encriptar por Algoritmo basado en Matriz")
            os.system('pause')

        elif s=='4':
            os.system('cls')
            print('Retornando....')
            os.system('pause')
            break
        else:
            os.system('cls')
            print("\n   Opcion no reconocida...\n")
            os.system('pause')
            continue

    elif ans=='2':
        os.system('cls')
        print(
            """
            Menu de Desencriptado
            --- Seleccione una de las siguiente opciones con los numeros ---
            [1] Desencriptar por Algoritmo Simetrico
            [2] Desencriptar por Algoritmo Asimetrico
            [3] Desencriptar por Algoritmo basado en Matriz
            [4] Retornar

            """)
        d = input("Que desea hacer? ")

        if d=='1':
            os.system('cls')
            print("\nDesencriptar por Algoritmo Simetrico")
            os.system('pause')

        elif d=='2':
            os.system('cls')
            print("\nDesencriptar por Algoritmo Asimetrico")
            os.system('pause')

        elif d=='3':
            os.system('cls')
            print("Desencriptar por Algoritmo basado en Matriz")
            os.system('pause')

        elif d=='4':
            os.system('cls')
            print('Retornando....')
            os.system('pause')
            break

        else:
            os.system('cls')
            print("\n   Opcion no reconocida...\n")
            os.system('pause')
            continue

    elif ans=='3':
        os.system('cls')
        print('Saliendo del programa....')
        os.system('pause')
        break


    else:
        os.system('cls')
        print("\n   Opcion no reconocida...\n")
        os.system('pause')
        continue
