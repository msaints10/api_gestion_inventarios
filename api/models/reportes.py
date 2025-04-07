from database.mysql_db import MysqlDB

class Reportes:
    def __init__(self):
        self.db = MysqlDB()

    def inventario_por_almacen(self, id_almacen: int):
        try:
            return self.db.call_procedure("Reporte_Inventario_Por_Almacen", [id_almacen], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de inventario por almacén: {str(e)}")

    def productos_stock_bajo(self):
        try:
            return self.db.call_procedure("Reporte_Productos_Stock_Bajo", [], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de productos con stock bajo: {str(e)}")

    def transacciones_por_fecha(self, fecha_inicio: str, fecha_fin: str):
        try:
            return self.db.call_procedure("Reporte_Transacciones_Por_Fecha", [fecha_inicio, fecha_fin], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de transacciones por fecha: {str(e)}")

    def productos_stocktotal_por_almacen(self, id_almacen: int):
        try:
            return self.db.call_procedure("reporte_productos_stocktotal_por_almacen", [id_almacen], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de stock total por almacén: {str(e)}")

    def transacciones_por_usuario(self, id_usuario: int):
        try:
            return self.db.call_procedure("reporte_transacciones_por_usuario", [id_usuario], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de transacciones por usuario: {str(e)}")

    def ventas_por_producto(self, id_producto: int):
        try:
            return self.db.call_procedure("reporte_ventas_por_producto", [id_producto], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de ventas por producto: {str(e)}")

    def movimiento_entre_almacenes(self, id_almacen_origen: int, id_almacen_destino: int):
        try:
            return self.db.call_procedure("reporte_movimiento_entre_almacenes", [id_almacen_origen, id_almacen_destino], expect_result=True)
        except Exception as e:
            raise Exception(f"Error al generar reporte de movimiento entre almacenes: {str(e)}")