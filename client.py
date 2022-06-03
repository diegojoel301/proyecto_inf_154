import socket

#mi_socket = socket.socket()

#mi_socket.connect( ('localhost', 8000) )

user = input("[+] Introduce tu username: ")

while True:
        mi_socket = socket.socket()

        mi_socket.connect( ('localhost', 8000) )

        mi_socket.send((f"<{user}>" + input(str(">"))).encode())

        respuesta = mi_socket.recv(1024)

        print(respuesta.decode())

        mi_socket.close()
