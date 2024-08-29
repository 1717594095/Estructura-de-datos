#arreglo bidimensional 3*3
arreg_bidim= [
    [20, 60, 70],
    [90, 10, 80],
    [30, 50, 40]
]

# Función para buscar un valor en la matriz
def buscar_valor(arreg_bidim, valor):
    for i in range(len(arreg_bidim)):
        for j in range(len(arreg_bidim[i])):
            if arreg_bidim[i][j] == valor:
                return i, j  # Retorna la posición si el valor se encuentra
    return None  # Retorna None si el valor no se encuentra

# Valor a buscar en la arreg_bidim
valor_buscado = 50

# Buscar el valor en la arreg_bidim
resultado = buscar_valor(arreg_bidim, valor_buscado)

# Mostrar resultados
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la arreg_bidim")



    # Crear una matriz bidimensional (3x3) para el ejemplo.txt
matriz = [
    [6, 7, 2], 
    [1, 5, 4],
    [8, 3, 9]
]

# Valor que estamos buscando
valor_buscado = 4

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")