def automata_finito(cadena):
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


f = open(input("[+] Introduce nombre del archivo a leer: "), "r")

salida = str()

for line in f:
	line = line.strip()

	for cadena in line.split(' '):
		salida += automata_finito(cadena)
	salida += "\n"

print(salida)
if input("[+] Deseas guardar la salida en un archivo? (Y/N): ").upper() == "Y":
	archivo_salida = open("salida.txt", "w")

	archivo_salida.write(salida)

	archivo_salida.close()
	
f.close()