from PracticaConsumo import PracticaConsumoDB

conexion = PracticaConsumoDB("root", "admin","localhost",  "tienda")

#conexion.mostrar_clientes()
conexion.guardar_cliente("HOMERO SIMPSON", "1990/08/04", "Av Siempre viva")
#conexion.mostrar_clientes()
#conexion.actualizar_cliente(11, "HOMERO SIMPSON", "1991/08/04", "BOULEVARD DONUT")
#conexion.eliminar_cliente(12)
conexion.mostrar_clientes()


