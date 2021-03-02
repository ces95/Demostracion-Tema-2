"""
Hecho por:

Cesar A. Diaz - 1075235
Salma Marmol - 108

"""

# Librerias
import os

#VARIABLES GLOBALES

ans = ''


#FUNCIONES



#INICIO DEL MENU DEL PROGRAMA
while ans :
    print(
        """
        Menu de Inicio
        --- Seleccione una de las siguiente opciones con los numeros ---
        [1] Encriptar un archivo 
        [2] Desencriptar un archivo 
        [3] Salir 

        """)
    
    ans = input("Que desea hacer? ")
    
    if ans=="1":
        os.system('cls')
        print(
        """
        Menu de Encriptado
        --- Seleccione una de las siguiente opciones con los numeros ---
        [1] Encriptar por 
        [2] Retornar 

        """)


    else:
    os.system("cls")
    print("\nopcion no reonocidad\n")
    continue