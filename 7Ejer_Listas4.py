archivo = open("romeo.txt")
palabras = []

for linea in archivo:
    lista_palabras = linea.split()
    for palabra in lista_palabras:
        if palabra not in palabras:
            palabras.append(palabra)

palabras.sort()

print(palabras)
