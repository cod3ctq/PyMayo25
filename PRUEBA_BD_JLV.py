from practicaconsumobd import PracticaConsumoBD

conexion = PracticaConsumoBD("root","admin","localhost",3306, "tienda")



#conexion.guardar_cliente("HOMERO SIMPSON", '2015/11/01',"BOULEVAR")
#conexion.actualizar_cliente(11,"HOMERO SIMPSON",'2010/01/01',"BOULEVARD DONUT")
#conexion.eliminar_cliente(11)
#conexion.mostrar_cliente()
#conexion.guardar_proveedor("Panadería Isabel", '22343212','jaime.leon@conocido.com')
#conexion.actualizar_proveedor(12,"Panadería Mónics", '123456','jaime@leon')
conexion.eliminar_proveedor(12)
conexion.mostrar_proveedor()
