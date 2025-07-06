# EJERCICIO 4 Crear una lista enlazada con 50 números enteros, del 1 al 999 generados aleatoriamente. Una vez creada la lista, vez creada la lista, se deben eliminar los nodos que estén fuera de un rango de valores leídos desde el teclado.

import random


# Definición del nodo de la lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_fuera_rango(self, minimo, maximo):
        # Eliminar nodos al inicio que estén fuera del rango
        while self.cabeza and (self.cabeza.dato < minimo or self.cabeza.dato > maximo):
            self.cabeza = self.cabeza.siguiente

        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.dato < minimo or actual.siguiente.dato > maximo:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

    def mostrar(self):
        actual = self.cabeza
        lista = []
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        print(lista)


# Crear la lista enlazada y agregar 50 números aleatorios
lista = ListaEnlazada()
for _ in range(50):
    num = random.randint(1, 999)
    lista.agregar(num)

print("Lista original:")
lista.mostrar()

# Leer rango desde teclado
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

# Eliminar nodos fuera del rango
lista.eliminar_fuera_rango(minimo, maximo)

print("Lista después de eliminar nodos fuera del rango:")
lista.mostrar()

# EJERCICIO 3 Implementar el método de búsqueda en la clase lista, el cual debe retornar el número de veces que se encuentra el dato dentro de la lista. de la lista. En caso de no encontrarse, el método debe mostrar un mensaje indicando que el dato no fue encontrado. El parámetro de entrada del método es el valor que se desea buscar.

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # ... otros métodos como agregar, eliminar, mostrar ...

    def buscar(self, valor):
        actual = self.cabeza
        contador = 0
        while actual:
            if actual.dato == valor:
                contador += 1
            actual = actual.siguiente

        if contador == 0:
            print(f"El dato {valor} no fue encontrado en la lista.")
        else:
            return contador
