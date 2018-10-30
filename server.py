#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver


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
        print("El cliente nos manda:")

        for line in self.rfile:
            mensaje = line.decode('utf-8').split(" ")
            #print("JULIA:", mensaje)
            if (line.decode('utf-8')[0:8] == "REGISTER"):
                self.dicc_registers[mensaje[1].split(':')[-1]] = [IP]
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                #print ("EN register:", line.decode('utf-8'))
                print (self.dicc_registers)

            elif (line == b'\r\n'):
                continue

            else:
                print(IP, "\t",self.client_address[1], "\t", line.decode('utf-8'))
                self.wfile.write(line)


if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', 6002), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
