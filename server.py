#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
if (len(sys.argv) == 2):
    PORT = int(sys.argv[1])
else:
    sys.exit("Usage: <PORT>")

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc_registers = {}
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        IP = self.client_address[0]
        print("Registro de clientes:")

        for line in self.rfile:
            mensaje = line.decode('utf-8').split(" ")
            #print("JULIA:", mensaje)
            if (mensaje[0] == "REGISTER"):
                user = mensaje[1].split(':')[1]
                self.dicc_registers[user] = [IP]
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            elif (mensaje[0] == "EXPIRES:"):
                EXPIRES = mensaje[1].split(':')[-1]
                if (EXPIRES == '0\r\n'):
                    del self.dicc_registers[user]
            elif (line == b'\r\n'):
                continue

            else:
                print(IP, "\t",self.client_address[1], "\t", line.decode('utf-8'))
                self.wfile.write(line)
        print(self.dicc_registers)

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
