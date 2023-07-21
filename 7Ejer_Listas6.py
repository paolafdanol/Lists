numeros = []

while True:
    entrada = input("Ingresa un número o escribe 'hecho' para terminar: ")
    if entrada == "hecho":
        break
    try:
        numero = float(entrada)
    except:
        print("Entrada inválida, por favor ingresa un número o escribe 'hecho'.")
        continue
    numeros.append(numero)

if len(numeros) > 0:
    print("Máximo:", max(numeros))
    print("Mínimo:", min(numeros))
else:
    print("No se ingresaron números.")
