from Cliente import Cliente
from Envios import Envio

class Saman_Delivery:
    def __init__(self):
        self.clientes = []
        self.envios = []

    def start(self):
        while True:
            print("----Bienvenido a Saman Delivery----\n\nPor favor elija una de las siguientes opciones: ")
            print("1. Registrar Clientes \n2. Crear Envio \n3. Mostrar Envios \n4. Salir del sistema")
            menu = input("---> ")

            if menu == '1':
                self.registrar_cliente()
            elif menu == '2':
                self.crear_envio()
            elif menu == '3':
                self.mostrar_envios()
            elif menu == '4':
                print("Saliendo del sistema!")
                break

    def registrar_cliente(self):
        nombre = input("Por favor ingrese su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        id = input("Por favor ingrese su cedula: ")
        direccion = input("Por favor ingrese su dirección de envio: ")
        telefono = input("Por favor ingrese su número de teléfono: ")

        client = Cliente(nombre, apellido, id, direccion, telefono)
        self.clientes.append(client)
        print("Cliente registrado exitosamente!")
        print()

    def crear_envio(self):
        while True: 
            cedula_cliente = input("Por favor ingrese la cédula del cliente: ")
            for cliente in self.clientes:
                if cedula_cliente == cliente.id:
                    contenido = input(f"Por favor ingrese el producto que se le enviará al {cliente.nombre}: ")
                    peso = int(input("Por favor ingrese el peso del producto a enviar (En Kg): "))
                    if peso < 7:
                        vehiculo = "Moto"
                        monto = peso * 2
                    elif peso >= 7:
                        vehiculo = "Carro"
                        monto = peso * 3
                    print("\nPor favor ingrese el estado de la dirección: ")
                    estado = input("1. Amazonas \n2. Anzoategui \n3. Apure \n4. Aragua \n5. Barinas \n6. Bolívar \n7. Carabobo \n8. Cojedes \n9. Delta Amacuro \n10. Distrito Capital \n11. Falcón \n12. Guárico \n13. La Guaira \n14. Lara \n15. Mérida \n16. Miranda \n17. Monagas \n18. Nueva Esparta \n19. Portuguesa \n20. Sucre \n21. Táchira \n22. Trujillo \n23. Yaracuy \n24. Zulia \n---> ")
                    if estado == "10" or estado == "16":
                        pass
                    else:
                        vehiculo = "Van"
                        monto = peso * 4.5
                    direccion_entrega = input("Ingrese la dirección de envio: ")
                    costo = monto * 1.35
                else:
                    print("Cliente no encontrado, por favor asegurese de que ingreso los datos correctos.")
            envio = Envio(contenido, vehiculo, costo, estado, direccion_entrega)
            self.envios.append(envio)
            print("Envio creado exitosamente")
            break

    def mostrar_envios(self):
        for envio in self.envios:
            for cliente in self.clientes:
                print()
                print("----Datos del Envio----")
                print(f"Contenido del Paquete: {envio.contenido}")
                print(f"Vehiculo: {envio.vehiculo}")
                print(f"Costo del Envio: {envio.costo}")
                print(f"Estado: {envio.estado}")
                print(f"Dirección del Cliente: {envio.direccion_entrega}")
                print("----Datos del Cliente----")