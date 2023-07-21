# Código original
#manejador = open('mbox-short.txt')
#contador = 0

#for linea in manejador:
#    palabras = linea.split()
    # print 'Depuración:', palabras
#    if len(palabras) == 0 : continue
#    if palabras[0] != 'From' : continue
#    print(palabras[2]) --- Linea no protegida

# Código modificado
manejador = open('mbox-short.txt')
contador = 0
for linea in manejador:
    palabras = linea.split()
    if len(palabras) < 3: continue # Protección adicional
    if len(palabras) == 0 : continue
    if palabras[0] != 'From' : continue
    print(palabras[2])




