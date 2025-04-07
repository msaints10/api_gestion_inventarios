import json
import datetime

import mysql.connector
from mysql.connector import Error, errorcode

from utils.settings import Settings


class MysqlDB:
    """
    Clase que proporciona una interfaz para la conexión con la base de datos MySQL.

    Attributes:
        settings (Settings): Instancia de la clase Settings.
        mysql_host (str): Host de la base de datos MySQL.
        mysql_port (str): Puerto de la base de datos MySQL.
        mysql_db (str): Base de datos de la base de datos MySQL.
        mysql_user (str): Usuario de la base de datos MySQL.
        mysql_password (str): Contraseña de la base de datos MySQL.
        connection (MySQLConnection): Instancia de la clase MySQLConnection.
    """

    def __init__(self):
        self.settings = Settings()
        self.mysql_host = self.settings.db_mysql_host
        self.mysql_port = self.settings.db_mysql_port
        self.mysql_db = self.settings.db_mysql_database
        self.mysql_user = self.settings.db_mysql_user
        self.mysql_password = self.settings.db_mysql_password
        self.connection = None

    def connect(self):
        """
        Método que permite la conexión con la base de datos MySQL.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.mysql_host,
                port=self.mysql_port,
                database=self.mysql_db,
                user=self.mysql_user,
                password=self.mysql_password,
            )
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception(
                    "Contraseña y/o usuario de la base de datos incorrecto")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("Base de datos no existe")
            elif err.errno == errorcode.CR_CONN_HOST_ERROR:
                raise Exception("Error de conexión cono MySQL")
            else:
                raise Exception(err)

    def disconnect(self):
        """
        Método que permite la desconexión con la base de datos MySQL.
        """
        if self.connection.is_connected():
            self.connection.close()

    def get_connection(self):
        """
        Método que retorna la conexión con la base de datos MySQL.

        Returns:
            MySQLConnection: Conexión con la base de datos MySQL.
        """
        return self.connection

    def commit(self):
        """
        Método que permite confirmar las transacciones en la base de datos MySQL.
        """
        self.connection.commit()

    def rollback(self):
        """
        Método que permite deshacer las transacciones en la base de datos MySQL.
        """
        self.connection.rollback()

    def execute_query_transaction(self, query: str, values: list = None):
        """
        Método que permite ejecutar una consulta en la base de datos MySQL dentro de una transacción.
        """
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute(query, values)
                self.commit()
        except Error as err:
            self.rollback()
            raise Exception(err)
        finally:
            cursor.close()
            self.disconnect()

    def execute_query(self, query: str, values: list = None):
        """
        Método que permite ejecutar una consulta en la base de datos MySQL.
        """
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute(query, values)
                return cursor.fetchall()
        except Error as err:
            raise Exception(err)
        finally:
            cursor.close()
            self.disconnect()
            
    def call_procedure(self, procedure_name: str, params: list = None, expect_result: bool = False):
        """
        Ejecuta un procedimiento almacenado.

        Args:
            procedure_name (str): Nombre del procedimiento.
            params (list): Parámetros del procedimiento.
            expect_result (bool): Indica si se espera que el procedimiento retorne datos.

        Returns:
            list: Resultados de la ejecución si expect_result=False.
        """
        cursor = None
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.callproc(procedure_name, params or [])
            if expect_result:
                result = []
                for res in cursor.stored_results():
                    result.extend(res.fetchall())
                return self.convert_retvaldate_tostr(result)
            self.commit()
        except Error as err:
            self.rollback()
            raise Exception(err)
        finally:
            if cursor:
                cursor.close()
            self.disconnect()
            
    def call_function(self, function_query: str, params: list = None):
        """
        Ejecuta una función SQL (SELECT funcion(param1, param2, ...)).

        Args:
            function_query (str): Query con SELECT y función.
            params (list): Lista de parámetros para la función.

        Returns:
            Resultado único de la función (por ejemplo, 1 o 0).
        """
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute(function_query, params or [])
                result = cursor.fetchone()
                return result[0] if result else None
        except Error as err:
            raise Exception(err)
        finally:
            cursor.close()
            self.disconnect()


    def convert_retvaldate_tostr(self, retval):
        """
        Convierte los valores de retorno que son de tipo datetime.datetime a string.
        Ahora también maneja tuplas que contienen objetos datetime.datetime.

        Args:
            retval: El valor de retorno a convertir. Puede ser una lista de diccionarios,
                    una lista de tuplas, o una tupla.

        Returns:
            El valor de retorno con los objetos datetime.datetime convertidos a string.
        """
        # Si retval es una tupla, la convertimos en una lista de una tupla para manejarla uniformemente
        if isinstance(retval, tuple):
            retval = [retval]

        for i, elemento in enumerate(retval):
            # Si el elemento es una tupla (como el ejemplo proporcionado)
            if isinstance(elemento, tuple):
                elemento_modificado = []
                for item in elemento:
                    if isinstance(item, datetime.datetime):
                        elemento_modificado.append(
                            item.strftime("%Y-%m-%dT%H:%M:%S"))
                    elif isinstance(item, str):
                        try:
                            # Intenta cargar el string como JSON
                            json_data = json.loads(item)
                            # Si es un JSON, procesa sus claves y valores
                            if isinstance(json_data, dict):
                                for clave, valor in json_data.items():
                                    if isinstance(valor, datetime.datetime):
                                        json_data[clave] = valor.strftime(
                                            "%Y-%m-%dT%H:%M:%S"
                                        )
                                item = json.dumps(json_data)
                        except json.JSONDecodeError:
                            # Si no es un JSON, deja el string como está
                            pass
                        elemento_modificado.append(item)
                    else:
                        elemento_modificado.append(item)
                retval[i] = tuple(elemento_modificado)
            # Aquí puedes agregar más lógica si necesitas manejar listas de diccionarios, etc.
        return retval

    def last_insert_id(self):
        """
        Método que retorna el último id insertado en la base de datos MySQL.
        """
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT LAST_INSERT_ID()")
                return cursor.fetchone()[0]
        except Error as err:
            raise Exception(err)
        finally:
            cursor.close()
            self.disconnect()