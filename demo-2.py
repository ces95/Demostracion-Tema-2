"""
Realizado por:

Cesar A. Diaz - 1075235
Salma Marmol - 1085618

"""

# LIBRERIAS
    #Para funciones del programa
import os
import sys
    #Para el encritado de la Matriz
import numpy as np
    #Para el encriptado Asimetrico
import rsa
from cryptography.fernet import Fernet #para la implementacion de la llave secreta
    #Para el encriptado Asimetrico
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


#FUNCIONES

#Metodos de Encriptado Asimetrico
def Create_RSA_Key():
    #crea la llave simetrica
    key = Fernet.generate_key()

    #escribe la llave simetrica a un file
    k = open('symmetric.key','wb')
    k.write(key)
    k.close()

    #crea las llaves publicas y privadas, de 2048 bits
    (pubkey,privkey)= rsa.newkeys(2048)

    #escribe la llave publica en un file
    pukey= open( 'publickey.key','wb')
    pukey.write(pubkey.save_pkcs1('PEM'))



    pukey.close()

    #escribe la llave privada en un file
    prkey= open('privkey.key','wb')
    prkey.write(privkey.save_pkcs1('PEM'))
    prkey.close()

def Encrypt_data_RSA():
    #abre el file de la llave simetrica
    simkey= open('symmetric.key','rb')
    key = simkey.read()

    #crea el cifrado
    cipher = Fernet(key)

    #abre el file para el cifrado
    myfile = open('cripto','rb')    #El archivo en este caso se llama cripto
    myfiledata = myfile.read()

    #cifra los datos
    encdata = cipher.encrypt(myfiledata)
    edata = open('encrypted_file','wb')
    edata.write(encdata)

    print(encdata)

    #abre el file de la llave publica
    pkey = open('publickey.key','rb')
    pkdata = pkey.read()

    #carga el file
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    #cifra el file de la llave simetrica con la llave publica
    enckey = rsa.encrypt(key,pubkey)

    #escribe la llave simetrica cifrada en un file
    ekey = open('encrypted_key','wb')
    ekey.write(enckey)

    print(enckey)

def Decrypt_data_RSA():

    #carga la llave privada para descifrar la llave publica
    prkey = open('privkey.key','rb')
    pkey = prkey.read()
    private_key = rsa.PrivateKey.load_pkcs1(pkey)

    e = open('encrypted_key','rb')
    ekey = e.read()

    dpubkey = rsa.decrypt(ekey,private_key)

    cipher= Fernet(dpubkey)

    encrypted_data =open('encrypted_file','rb')
    edata = encrypted_data.read()

    decrypted_data = cipher.decrypt(edata)

    print(decrypted_data.decode())

#Metodos de Encriptado Simetrico

def Encrypt_data_AES():
    key = get_random_bytes(32) # Genera la llave
    dataenc = 'Esto es tarea de criptografia!' # Son los datos

    # === Cifrado ===

    # Convierte los datos en bytes, usando .encode
    data = dataenc.encode('utf-8')

    #Crea el objecto de cifrado, y cifra los datos
    cipherenc = AES.new(key, AES.MODE_CFB)
    ciphbytes = cipherenc.encrypt(data)

    # Aqui se presentan nuestros datos
    iv = cipherenc.iv
    ciphdata = ciphbytes

    print(ciphdata)

def Decrypt_data_AES():


#Funcion MAIN - Para el menu del programa
def main():
    ans = True
    while ans :
        os.system('cls')
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
                print("\nEncriptar por Algoritmo Simetrico RSA\n")
                Encrypt_data_AES()
                os.system('pause')

            elif s=='2':
                os.system('cls')
                print("\nEncriptar por Algoritmo Asimetrico\n")
                Create_RSA_Key()
                Encrypt_data_RSA()
                os.system('pause')


            elif s=='3':
                os.system('cls')
                print("\nEncriptar por Algoritmo basado en Matriz\n")
                os.system('pause')

            elif s=='4':
                os.system('cls')
                print('\nRetornando....\n\n')
                os.system('pause')
                continue
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
                print("\nDesencriptar por Algoritmo Simetrico\n")
                Decrypt_data_AES()
                os.system('pause')

            elif d=='2':
                os.system('cls')
                print("\nDesencriptar por Algoritmo Asimetrico\n")
                Decrypt_data_RSA()
                os.system('pause')

            elif d=='3':
                os.system('cls')
                print("\nDesencriptar por Algoritmo basado en Matriz\n")
                os.system('pause')

            elif d=='4':
                os.system('cls')
                print('\nRetornando....\n\n')
                os.system('pause')
                continue

            else:
                os.system('cls')
                print("\n   Opcion no reconocida...\n")
                os.system('pause')
                continue

        elif ans=='3':
            os.system('cls')
            print('Saliendo del programa.... \n')
            break

        else:
            os.system('cls')
            print("\n   Opcion no reconocida...\n")
            os.system('pause')
            continue

#INICIO DEL MENU DEL PROGRAMA
main()
