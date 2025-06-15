class Estudiante:
    def __init__(self, id, nombres, apellidos, direccion, telefonos):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefonos = telefonos  # Lista de 3 teléfonos

    def mostrar_informacion(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombres} {self.apellidos}")
        print(f"Dirección: {self.direccion}")
        print("Teléfonos:")
        for tel in self.telefonos:
            print(f"- {tel}")

# Crear un objeto Estudiante con datos de ejemplo
telefonos_estudiante = ["0987654321", "0991234567", "0976543210"]
estudiante1 = Estudiante(
    id=1,
    nombres="Carlos Alberto",
    apellidos="Salgado Vélez",
    direccion="Av. Central #123, Quito",
    telefonos=telefonos_estudiante
)

# Mostrar información del estudiante
estudiante1.mostrar_informacion()
