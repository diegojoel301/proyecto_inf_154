import socket
def automata_finito(caracter):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
                'l', 'm', 'n', 'ñ', 'o','p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', ' ']

        TablaT = [['ini', 'a', '.-'], ['ini', 'b', '-..'], ['ini', 'c', '-.-.'], 
                ['ini', 'd', '-..'], ['ini', 'e', '.'], ['ini', 'f', '..-.'], ['ini', 'g', '--.'],
                ['ini', 'h', '....'], ['ini', 'i', '..'], ['ini', 'j', '.---'], ['ini', 'k', '-.-'],
                ['ini', 'l', '.-..'], ['ini', 'm', '--'], ['ini', 'n', '-.'], ['ini', 'ñ', '--.--'],
                ['ini', 'o', '---'], ['ini', 'p', '.--.'], ['ini', 'q', '--.-'], ['ini', 'r', '.-.'],
                ['ini', 's', '...'], ['ini', 't', '-'], ['ini', 'u', '..-'], ['ini', 'v', '...-'], 
                ['ini', 'w', '.--'], ['ini', 'x', '-..-'], ['ini', 'y', '-.--'], ['ini', 'z', '--..'],
                ['ini', ' ', '/']]

        bandera = True

        TablaC = [] # Tabla para almacenar los estados que se mueven

        EI = 'ini' # Estado inicial q0

        EF = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', 
                '..', '.---', '-.-', '.-..', '--', '-.', '--.--',  '---', '.--.', '--.-', 
                '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', 
                '/', 'ini'] # Estado Final qf

        EA = EI # Estado Actual

        # Verificar que el caracter pertenezca al alphabet
        if caracter in alphabet:
                # Buscar en la tabla el caracter
                for f in TablaT:
                        # Recorrer las transiciones de la tabla
                        # Indicar el estado actual y el estado final
                        if caracter == f[1] and EA == f[0]:
                                # Agregar elementos a la tabla comparativa
                                TablaC.append([EA, caracter, f[2]])
                                # Actualizar el estado
                                EA = f[2]
                                break
        else:
                print("Cadena no pertenece al alfabeto: " + caracter)
                bandera = False

        # Comparar si el estado actual es igual al estado final

        if EA in EF and bandera == True:
                return EA
        return "-1"

def codifica_cadena(cadena):
        salida = str()
        for caracter in cadena:
                salida += automata_finito(caracter) + " "
        return salida[0:len(salida) - 1]

while True:
        mi_socket = socket.socket()

        mi_socket.connect( ('192.168.146.128', 8000) )

        #print(mensaje)

        mi_socket.send(codifica_cadena(input(str(">"))).encode())

        respuesta = mi_socket.recv(1024)

        print(respuesta.decode())

        mi_socket.close()
