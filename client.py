#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente UDP que abre un socket a un servidor."""

import socket
import sys
# Constantes. Dirección IP del servidor y contenido a enviar
if(len(sys.argv) > 3):

    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    R = sys.argv[3]
    list_line = sys.argv[3:]
    LINE = " ".join(list_line)

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((SERVER, PORT))
        if (R == "REGISTER" and len(sys.argv) >= 5):
            USER = sys.argv[4]
            TIME = int(sys.argv[5])
            REGISTER = 'REGISTER sip:' + USER + ' SIP/2.0\r\n'
            EXPIRES = REGISTER + 'EXPIRES: ' + str(TIME) + '\r\n'
            my_socket.send(bytes(EXPIRES, 'utf-8'))
            print(EXPIRES)
        else:
            print("Enviando:", SERVER, PORT, LINE)
            my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))

    print("Socket terminado.")
else:
    print("Introducir IP, PUERTO, Mensaje.")
