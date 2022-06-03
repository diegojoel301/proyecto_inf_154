def automata_finito(cadena):
	alphabet = ['.', '/', '-']

	TablaT = [['ini', '-', 't'], ['ini', '/', ' '], ['ini', '.', 'e'],
				['t', '-', 'm'], ['t', '.', 'n'], ['e', '-', 'a'], ['e', '.', 'i'],
				['m', '-', 'o'], ['m', '.', 'g'], ['n', '-', 'k'], ['n', '.', 'd'],
				['a', '-', 'w'], ['a', '.', 'r'], ['i', '-', 'u'], ['i', '.', 's'],
				['g', '-', 'q'], ['g', '.', 'z'], ['k', '-', 'y'], ['k', '.', 'c'],
				['d', '-', 'x'], ['d', '.', 'b'], ['w', '-', 'j'], ['w', '.', 'p'],
				['r', '.', 'l'], ['u', '.', 'f'], ['s', '-', 'v'], ['s', '.', 'h'],
				['q', '-', 'ñ']]

	bandera = True

	TablaC = [] # Tabla para almacenar los estados que se mueven

	EI = 'ini' # Estado inicial q0

	EF = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
		'l', 'm', 'n', 'ñ','o','p', 'q', 'r', 's', 't', 'u', 'v',
		'w', 'x', 'y', 'z', ' '] # Estado Final qf

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
			bandera = False
			break
	# Comparar si el estado actual es igual al estado final

	if EA in EF and bandera == True:
		return EA
	return "-1"


f = open(input("[+] Introduce nombre del archivo a leer: "), "r")

salida = str()

for line in f:
	line = line.strip()

	for morse_code in line.split(' '):
		salida += automata_finito(morse_code)
	salida += "\n"

print(salida)
if input("[+] Deseas guardar la salida en un archivo? (Y/N): ").upper() == "Y":
	archivo_salida = open("salida.txt", mode = "w", encoding = "utf-8")

	archivo_salida.write(salida)

	archivo_salida.close()

f.close()

