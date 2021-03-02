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
from egcd import egcd #pip install egcd
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

def Encrypt_data_AES(dataenc):
    key = get_random_bytes(32) # Genera la llave
    #dataenc = input('Escriba el texto que desea encriptar \n') # Son los datos

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

def Decrypt_data_AES(dataenc):
    key = get_random_bytes(32) # Genera la llave
    dataenc1 = dataenc # Son los datos

    # === Cifrado ===

    # Convierte los datos en bytes, usando .encode
    data = dataenc1.encode('utf-8')

    #Crea el objecto de cifrado, y cifra los datos
    cipherenc = AES.new(key, AES.MODE_CFB)
    ciphbytes = cipherenc.encrypt(data)

    # Aqui se presentan nuestros datos
    iv = cipherenc.iv
    ciphdata = ciphbytes
    # Crea el objeto de cifrado y decifra los datos
    ciphdec = AES.new(key, AES.MODE_CFB, iv=iv)
    decbytes = ciphdec.decrypt(ciphdata)

    # Convierte los bytes a string
    decdata = decbytes.decode('utf-8')

    print(decdata)
    # === Prueba para comparar los datos ===

    assert dataenc1 == decdata, 'La data original no concuerda con el resultado'

#Metodos de Encriptado por Matriz
"""
Notas para Hill Cipher!
    Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)
C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.@?" #mod 57
#alphabet = "abcdefghijklmnopqrstuvwxyz " #mod 27

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def Matrix_mod_inv(matrix,modu):

    """
    En este metodo es necesario buscar la inversa del modulo de la matriz, para ello es necesario
    1- Encontrar el determinante de la Matriz
    2- Encontrar el determinante en el valor especifico del modulo (osea la longitud del alfabeto)

    """
    det = int(np.round(np.linalg.det(matrix)))  # 1
    det_inv = egcd(det, modu)[1] % modu  # 2
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modu)

    return Matrix_mod_inv

def Encrypt_HC(message, K):

    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted

def Derypt_HC(cipher, Kinv):


    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted

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
                dataenc = input('Escriba el texto que desea encriptar \n') # Son los dato
                Encrypt_data_AES(dataenc)
                os.system('pause')

            elif s=='2':
                os.system('cls')
                print("\nEncriptar por Algoritmo Asimetrico\n")
                Create_RSA_Key()
                Encrypt_data_RSA()
                os.system('pause')


            elif s=='3':
                os.system('cls')
                print("\nEncriptar por Algoritmo de Matriz Hill Cipher\n")

                message = input("\nEscriba el mnesaje que desee cifrar:\n")
                # K = np.matrix([[3, 3], [2, 5]])
                # K = np.matrix([[6, 24, 1], [13,16,10], [20,17,15]]) # for length of alphabet = 26
                K = np.matrix([[3,10,20],[20,19,17], [23,78,17]]) # for length of alphabet = 27


                #Matrix_mod_inv(matrix,modu)
                encrypted_message = Encrypt_HC(message,K)
                print("\n"+"Original message: " + message)
                print("Encrypted message: " + encrypted_message+"\n")
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
                Decrypt_data_AES(dataenc)
                os.system('pause')

            elif d=='2':
                os.system('cls')
                print("\nDesencriptar por Algoritmo Asimetrico\n")
                Decrypt_data_RSA()
                os.system('pause')

            elif d=='3':
                os.system('cls')
                print("\nDesencriptar por Algoritmo basado en Matriz\n")
                Kinv = Matrix_mod_inv(K, len(alphabet))
                #Derypt_HC(cipher, Kinv)


                decrypted_message = Derypt_HC(encrypted_message, Kinv)
                print("Encrypted message: " + encrypted_message+"\n")
                print("Decrypted message: " + decrypted_message+"\n")
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
