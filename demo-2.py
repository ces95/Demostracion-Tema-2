"""
Realizado por:

Cesar A. Diaz - 1075235
Salma Marmol - 108

"""

# Librerias
import os




#FUNCIONES
def simetrico():
    print('')

def asimetrico():
    print('')

def matricial():
    print('')


def main():
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

        elif ans=='2':
            os.system('cls')

        elif ans=='3':
            os.system('cls')

        elif ans=='4':
            os.system('cls')


        else:
            os.system('cls')
            print("\n   Opcion no reconocida...\n")
            os.system('pause')
            continue

#INICIO DEL MENU DEL PROGRAMA
main()