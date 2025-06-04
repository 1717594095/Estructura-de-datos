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
        # Crear una instancia de rectángulo con largo 10 y ancho 4
    rectangulo = Rectangulo(10, 4)
    print("Rectángulo:")
    print(f"Área: {rectangulo.calcular_area():.2f}")
    print(f"Perímetro: {rectangulo.calcular_perimetro():.2f}")
