import sqlite3

class IterableCategoria(type):
    def __iter__(cls):
        return iter(cls.__name__)

class Categoria(object):
    __metaclass__ = IterableCategoria
    def __init__(self, codigo:int=None, nombre:str=None):
        self.codigo = codigo
        self.nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, pcodigo):
        self.__codigo = pcodigo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, pnombre):
        self.__nombre = pnombre

    ## OBTENER CATEGORIAS DE PRODUCTOS
    ## OBTENER PROVEEDOR
    def obtenerCategorias(self):
        dato=None
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                SELECT *
                FROM categoria
                '''
            cursor.execute(query)
            dato = cursor.fetchall()
            return dato

        except Exception as e:
            print("Error: {}".format(e))
        finally:
                database.close()
        return dato