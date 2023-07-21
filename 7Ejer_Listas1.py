def recortar(lista):
    if len(lista) < 2:
        return None
    else:
        del lista[-1]
        del lista[0]
        return None

def medio(lista):
    if len(lista) < 3:
        return []
    else:
        return lista[1:-1]

# Pedimos al usuario que ingrese una lista
input_str = input("Ingresa una lista de números separados por comas: ")

# Convertimos la entrada en una lista de números
input_list = [int(i) for i in input_str.split(",")]

# Llamamos a la función recortar para modificar la lista original
recortar(input_list)

# Llamamos a la función medio para obtener una nueva lista
output_list = medio(input_list)

# Imprimimos la lista original y la nueva lista resultante
print("Lista original:", input_list)
print("Lista resultante:", output_list)
