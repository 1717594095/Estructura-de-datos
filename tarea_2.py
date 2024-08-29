# arreglo bidimensional 3*3
arreg_bidim = [
    [12, 5, 7],
    [1, 15, 9],
    [8, 3, 10]
]

# Función para ordenar una fila específica utilizando Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Mostrar el arreglo bidimensional 3*3 original
print("arreg_bidim original:")
for fila in arreg_bidim:
    print(fila)

# Fila a ordenar (índice de fila 1, que corresponde a la segunda fila)
fila_a_ordenar = 1
bubble_sort(arreg_bidim[fila_a_ordenar])

# Mostrar el arreglo bidimensional después de ordenar la fila especificada
print("\narreg_bidim con la fila 1 ordenada:")
for fila in arreg_bidim:
    print(fila)


