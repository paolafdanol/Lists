nombre_archivo = input("Ingresa el nombre del archivo: ")
archivo = open(nombre_archivo)
contador = 0

for linea in archivo:
    if linea.startswith("From "):
        contador += 1
        palabras = linea.split()
        print(palabras[1])

print("Total de líneas From:", contador)

