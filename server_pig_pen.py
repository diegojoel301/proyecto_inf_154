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

mi_socket = socket.socket()
mi_socket.bind( ('192.168.146.128', 8000) )

mi_socket.listen(5)

while True:
	conexion, addr = mi_socket.accept()
	#print("Nueva conexion establecida".encode())
	#print(addr)

	peticion = conexion.recv(1024).decode()

	salida = str()

	for linea in peticion[0:len(peticion) - 1].split('\n'):
		#print(linea)
		salida += decodificacion_cadena(linea) + "\n"

	print(salida)

	conexion.close()
