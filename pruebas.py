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
    list_registers = []
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """

        print("El cliente nos manda:")
        for line in self.rfile:
                print (line)
                if (line[0:8] == "REGISTER"):
                    list_registers = [self.client_address[0],line[9:]]
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                    print (list_registers)
                else:
                    print(self.client_address[0], "\t", self.client_address[1], "\t", line.decode('utf-8'))
                    self.wfile.write(line)


if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', 6001), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
