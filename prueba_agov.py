from practicaconsumo import PracticaConsumoDB

conexion = PracticaConsumoDB("db1", "admin",
                             "localhost", 1521, "XE")
conexion.mostrar_cliente()
# conexion.guardar_cliente("Homero Simpson",
#                          "04/08/19", "Av. Siempreviva")
# conexion.actualizar_cliente(21, "Homero Simpson",
#                             "04/08/90", "Blvd Donut")
# conexion.eliminar_cliente(21)