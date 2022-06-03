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


f = open(input("[+] Introduce nombre del archivo a leer: "), mode = "r", encoding = "utf-8")

salida = str()

for line in f:
	line = line.strip()

	for caracter in line:
		salida += automata_finito(caracter.lower()) + " "
	salida += "\n"

print(salida)
if input("[+] Deseas guardar la salida en un archivo? (Y/N): ").upper() == "Y":
	archivo_salida = open("salida.txt", "w")

	archivo_salida.write(salida)

	archivo_salida.close()

f.close()

