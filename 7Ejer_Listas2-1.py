manejador = open('archivo.txt')
contador = 0
for linea in manejador:
    palabras = linea.split()
    if len(palabras) < 3: continue # proteger línea 6
    if len(palabras) == 0 : continue
    if palabras[0] != 'From' : continue
    if len(palabras) >= 3:
        print(palabras[2])
    contador += 1
print("Se procesaron", contador, "líneas en total.")


