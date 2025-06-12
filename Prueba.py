from PracticaConsumo import PracticaConsumoDB

conexion = PracticaConsumoDB("db1", "admin", "192.168.186.1", 1521, "XE")

conexion.mostrar_clientes()

conexion.guardar_cliente("HOMERO SIMPSON", "04/08/1990", "AVENIDA SIEMPREVIVA")

conexion.actualizar_cliente(11, "HOMERO SIMPSON", "04/08/2006", "BOOULEVARD DONUT")

conexion.eliminar_cliente(12)
conexion.mostrar_clientes()
