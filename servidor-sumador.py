#!/usr/bin/python3
"""
Ejercicio Servidor Calculadora: Programa que funciona como Server.
Debemos pasarle en la URL al servidor la operacion que queremos realizar seguida de los valores con los que queremos operar. Debe mostrar el resultado al usuario. 
Juan Ureña
j.urenag@alumnos.urjc.es
SAT(URJC)
"""

#Importamos paquetes necesarios

import socket
import random

#Creamos TCP socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Comprobamos si está en uso el puerto
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Atamos al puerto
name=socket.gethostname()
mySocket.bind((name, 1234))

#Fijamos número máximo de usuarios a 5
mySocket.listen(5)

#Estamos listos para recibir solicitudes

#Parte Principal


try:
    while True:
#Genero URL aleatoria
        nextNum = random.randrange(999999999)
        nextUrl =str(nextNum)
#Recibo mensaje
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        
        info=recvSocket.recv(2048).split()[1]
#Envio mensaje
        recvSocket.close()
        print('info')
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()



