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
import calculadora

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
#Recibo mensaje
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        
        request=str(recvSocket.recv(2048), 'utf-8')
        resource=request.split()[1]
        
        try:
        
            _, num1, operation, num2=resource.split('/')
            print (num1)
            print (operation)
            print (num2)
            
        
            result=calculadora.function[operation](float(num1),float(num2))
            result="El resultado de la operacion es: "+ result
        
            print(result)
           
        except:
            result=('<p>Error: La entrada debe ser: '+
            'hostname:1234/num1/operacion/num2.</p>'+
            '<p>Operaciones: suma, resta, multiplicacion, division.</p>')   
        
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Calculadora Online</h1>" +
                        bytes(result, 'utf-8') +
                        b"</body></html>" +
                        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()



