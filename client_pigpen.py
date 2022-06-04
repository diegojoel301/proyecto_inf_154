import socket

def automata_finito_decodificador(cadena):
	alphabet = ['_', '|', ']', '[', '-', '/', '.', 'v', '^', '<', '>']

	TablaT = [['ini', '_', 's1'], ['ini', '|', 's2'], ['ini', ']', 'd'], ['ini', '[', 'f'],
				['ini', '-', 's4'], ['ini', '.', 's7'], ['ini', '/', ' '], ['ini', 'v', 's'],
				['ini', '>', 't'], ['ini', '<', 'u'], ['ini', '^', 'v'],  ['s1', '|', 'a'],
				['s2', '_', 'c'], ['s2', '-', 'i'], ['s2', '.', 's3'], ['f', '.', 'o'],
				['f', ']', 'e'], ['s4', '|', 'g'], ['s7', '_', 's5'], ['s7', ']', 'm'],
				['s7', '-', 's6'], ['s7', 'v', 'w'], ['s7', '>', 'x'], ['s7', '<', 'y'],
				['s7', '^', 'z'], ['c', '|', 'b'], ['i', '|', 'h'], ['s3', '-', 'r'],
				['s3', '_', 'l'], ['o', ']', 'n'], ['s5', '|', 'j'], ['s6', '|', 'p'],
				['r', '|', 'q'], ['l', '|', 'k']]

	bandera = True

	TablaC = [] # Tabla para almacenar los estados que se mueven

	EI = 'ini' # Estado inicial q0

	EF = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
		'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v','w',
		'x', 'y', 'z', '/', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 'ini', ' '] # Estado Final qf

	EA = EI # Estado Actual

	for caracter in cadena:
		# Verificar que el caracter pertenezca al alphabet = ['x']
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


def decodificacion_cadena(cadena):
	salida = str()

	for caracter in cadena.split(' '):
		salida = salida + automata_finito_decodificador(caracter)
	return salida


def automata_finito_codificador(caracter):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
		'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', ' ']

	TablaT = [['ini', 'a', '_|'], ['ini', 'b', '|_|'], ['ini', 'c', '|_'], 
		['ini', 'd', ']'], ['ini', 'e', '[]'], ['ini', 'f', '['], ['ini', 'g', '-|'],
		['ini', 'h', '|-|'], ['ini', 'i', '|-'], ['ini', 'j', '._|'], ['ini', 'k', '|._|'],
		['ini', 'l', '|._'], ['ini', 'm', '.]'], ['ini', 'n', '[.]'], ['ini', 'o', '[.'],
		['ini', 'p', '.-|'], ['ini', 'q', '|.-|'], ['ini', 'r', '|.-'], ['ini', 's', 'v'], 
		['ini', 't', '>'], ['ini', 'u', '<'], ['ini', 'v', '^'], ['ini', 'w', '.v'],
		['ini', 'x', '.>'], ['ini', 'y', '.<'], ['ini', 'z', '.^'], ['ini', ' ', '/']]

	bandera = True

	TablaC = [] # Tabla para almacenar los estados que se mueven

	EI = 'ini' # Estado inicial q0

	EF = ['_|', '|_|', '|_', ']', '[]', '[', '-|', '|-|', '|-', '._|',
		 '|._|', '|._', '.]', '[.]', '[.', '.-|', '|.-|', '|.-', 'v', 
		 '>', '<', '^', '.v', '.>', '.<', '.^', 'ini', '/'] # Estado Final qf

	EA = EI # Estado Actual

	# Verificar que el caracter pertenezca al alphabet = ['x']
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
                salida += automata_finito_codificador(caracter) + " "
        return salida[0:len(salida) - 1]


mi_socket = socket.socket()

mi_socket.connect( ('192.168.146.139', 8000) )

f = open(input("[+] Introduce nombre del archivo a enviar: "), mode = "r")

mensaje = str()


for line in f:
	line = line.strip()

	mensaje += codifica_cadena(line) + "\n"

print(mensaje[0:len(mensaje) - 1])

mi_socket.send(mensaje.encode())

mi_socket.close()
f.close()
