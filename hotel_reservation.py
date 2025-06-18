# hotel_reservation.py

# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # Ej: 'simple', 'doble', 'suite'
        self.precio = precio
        self.esta_reservada = False

    def reservar(self):
        if not self.esta_reservada:
            self.esta_reservada = True
            print(f"Habitación {self.numero} ha sido reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def cancelar_reserva(self):
        if self.esta_reservada:
            self.esta_reservada = False
            print(f"Reserva de la habitación {self.numero} ha sido cancelada.")
        else:
            print(f"La habitación {self.numero} no está reservada.")

    def mostrar_info(self):
        estado = "Reservada" if self.esta_reservada else "Disponible"
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Estado: {estado}")

# Clase que representa al cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        print(f"Cliente: {self.nombre} | Cédula: {self.cedula}")

# Clase que representa el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.habitaciones = []
        self.reservas = {}

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, numero_habitacion, cliente):
        for hab in self.habitaciones:
            if hab.numero == numero_habitacion:
                if not hab.esta_reservada:
                    hab.reservar()
                    self.reservas[numero_habitacion] = cliente
                    return
                else:
                    print("La habitación ya está reservada.")
                    return
        print("Habitación no encontrada.")

    def mostrar_habitaciones(self):
        for hab in self.habitaciones:
            hab.mostrar_info()

    def mostrar_reservas(self):
        for numero, cliente in self.reservas.items():
            print(f"Habitación {numero} reservada por {cliente.nombre}")

# Ejemplo de uso del sistema
if __name__ == "__main__":
    sistema = SistemaReservas()

    # Crear habitaciones
    h1 = Habitacion(101, "simple", 50)
    h2 = Habitacion(102, "doble", 80)
    h3 = Habitacion(201, "suite", 120)

    sistema.agregar_habitacion(h1)
    sistema.agregar_habitacion(h2)
    sistema.agregar_habitacion(h3)

    # Mostrar todas las habitaciones
    print("Estado inicial de las habitaciones:")
    sistema.mostrar_habitaciones()

    # Crear cliente y hacer reserva
    cliente1 = Cliente("Ana Pérez", "1234567890")
    sistema.reservar_habitacion(102, cliente1)

    # Mostrar estado actualizado
    print("\nDespués de la reserva:")
    sistema.mostrar_habitaciones()
    sistema.mostrar_reservas()
