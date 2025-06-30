# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostrar la lista por pantalla
print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print("-", asignatura)

    # Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostrar el mensaje para cada asignatura
for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

# Lista para almacenar los números ganadores
numeros_ganadores = []

# Pedir al usuario los 6 números ganadores
print("Introduce los 6 números ganadores de la lotería primitiva:")

for i in range(6):
    while True:
        try:
            numero = int(input(f"Número {i+1}: "))
            if 1 <= numero <= 49:
                if numero not in numeros_ganadores:
                    numeros_ganadores.append(numero)
                    break
                else:
                    print("Ese número ya ha sido introducido. Introduce un número diferente.")
            else:
                print("El número debe estar entre 1 y 49.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

# Ordenar la lista
numeros_ganadores.sort()

# Mostrar los números ordenados
print("\nNúmeros ganadores ordenados de menor a mayor:")
print(numeros_ganadores)

# Crear la lista con los números del 1 al 10
numeros = list(range(1, 11))

# Invertir la lista
numeros.reverse()

# Mostrar los números separados por comas
print(", ".join(str(num) for num in numeros))

import string

# Crear la lista del abecedario
abecedario = list(string.ascii_lowercase)

# Eliminar las letras en posiciones múltiplos de 3 (1-based index)
resultado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]

# Mostrar la lista resultante
print("Letras restantes:")
print(resultado)

