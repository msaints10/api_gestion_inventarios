from database.mysql_db import MysqlDB

class Inventario:
    def __init__(self):
        self.db = MysqlDB()

    def registrar(self, id_producto: int, id_almacen: int, cantidad: int):
        try:
            self.db.call_procedure("registrar_inventario", [id_producto, id_almacen, cantidad])
            return {"mensaje": "Inventario registrado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al registrar inventario: {str(e)}")

    def actualizar(self, id_inventario: int, id_producto: int, id_almacen: int, cantidad: int):
        try:
            self.db.call_procedure("actualizar_inventario", [id_inventario, id_producto, id_almacen, cantidad])
            return {"mensaje": "Inventario actualizado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al actualizar inventario: {str(e)}")

    def eliminar(self, id_inventario: int):
        try:
            self.db.call_procedure("eliminar_inventario", [id_inventario])
            return {"mensaje": "Inventario eliminado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al eliminar inventario: {str(e)}")

    def obtener(self, id_inventario: int):
        try:
            return self.db.call_procedure("obtener_inventario", [id_inventario], True)
        except Exception as e:
            raise Exception(f"Error al obtener inventario: {str(e)}")

    def obtener_todos(self):
        try:
            return self.db.call_procedure("obtener_inventarios", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener inventarios: {str(e)}")
