def esta_balanceado(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for simbolo in expresion:
        if simbolo in '([{':
            pila.append(simbolo)
        elif simbolo in ')]}':
            if not pila or pila[-1] != pares[simbolo]:
                return False
            pila.pop()

    return len(pila) == 0


def mover_disco(origen, destino, nombre_origen, nombre_destino):
    disco = origen.pop()
    destino.append(disco)
    print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")


def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino):
    if n == 1:
        mover_disco(origen, destino, nombre_origen, nombre_destino)
    else:
        hanoi(n - 1, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar)
        mover_disco(origen, destino, nombre_origen, nombre_destino)
        hanoi(n - 1, auxiliar, origen, destino, nombre_auxiliar, nombre_origen, nombre_destino)


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Verificar paréntesis balanceados")
        print("2. Resolver Torres de Hanoi")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            expresion = input("Ingrese una expresión matemática: ")
            if esta_balanceado(expresion):
                print("Fórmula balanceada.")
            else:
                print("Fórmula desbalanceada.")

        elif opcion == '2':
            try:
                n = int(input("Ingrese el número de discos: "))
                if n <= 0:
                    print("Debe ser un número positivo.")
                    continue

                origen = list(reversed(range(1, n + 1)))
                auxiliar = []
                destino = []

                print("\nPasos para resolver las Torres de Hanoi:")
                hanoi(n, origen, auxiliar, destino, 'Origen', 'Auxiliar', 'Destino')

            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == '3':
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
menu()
