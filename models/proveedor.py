import sqlite3

class Proveedor(object):
    def __init__(self, codigo:int=None, nombre:str=None, direccion:str=None, ruc:int=None, password:str=None):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion= direccion
        self.ruc = ruc
        self.password = password

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, pcodigo):
        self.__codigo = pcodigo

    @property
    def nombre(self):
        return self.__nombre
    @codigo.setter
    def nombre(self, pnombre):
        self.__nombre = pnombre

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, pdireccion):
        self.__direccion = pdireccion

    @property
    def ruc(self):
        return self.__ruc
    @ruc.setter
    def ruc(self, pruc):
        self.__ruc = pruc

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value



    
    ## CREAR CUENTA
    def crearProveedor(self) -> bool:
        status  = False
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            INSERT INTO proveedor(nombre, direccion, ruc, password)
            VALUES ('{}', '{}', {}, '{}')
            '''.format(self.__nombre, self.__direccion, self.__ruc, self.__password)

            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY

            status = True

        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return status

    ## OBTENER PROVEEDOR
    def obtenerProveedor(self, ruc:str):
        dato=None
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                SELECT *
                FROM proveedor WHERE ruc = '{}'
                '''.format(ruc)

            cursor.execute(query)
            dato = cursor.fetchone()
            

            return dato

        except Exception as e:
            print("Error: {}".format(e))
        finally:
                database.close()
        return dato