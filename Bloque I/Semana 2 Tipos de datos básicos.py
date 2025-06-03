import math

# Clase que representa un círculo
class Circulo:
    def __init__(self, radio):
        # Inicializa el radio del círculo
        self.radio = radio

    def calcular_area(self):
        # Retorna el área del círculo: pi * r^2
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        # Retorna el perímetro (circunferencia): 2 * pi * r
        return 2 * math.pi * self.radio

# Clase que representa un rectángulo
class Rectangulo:
    def __init__(self, largo, ancho):
        # Inicializa largo y ancho del rectángulo
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        # Retorna el área: largo * ancho
        return self.largo * self.ancho

    def calcular_perimetro(self):
        # Retorna el perímetro: 2 * (largo + ancho)
        return 2 * (self.largo + self.ancho)

# Bloque principal de prueba
if __name__ == "__main__":
    # Crear una instancia de círculo con radio 5
    circulo = Circulo(5)
    print("Círculo:")
    print(f"Área: {circulo.calcular_area():.2f}")
