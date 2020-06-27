import sqlite3

class IterableProducto(type):
    def __iter__(cls):
        return iter(cls.__name__)


class Producto(object):
    __metaclass__ = IterableProducto
    def __init__(self, codigo:str, nombre: str, descripcion: str, precio: float, stock: int, categoria: int, tienda:str):
        self.__codigo       = None
        self.__nombre       = nombre
        self.__descripcion  = descripcion
        self.__precio       = precio
        self.__stock        = stock
        self.__categoria    = categoria
        self.__tienda       = tienda

    ## GETTER ##
    @property
    def getCodigo(self) -> str:
        return self.__codigo

    @property
    def getNombre(self) -> str:
        return self.__nombre

    @property
    def getDescripcion(self) -> str:
        return self.__descripcion

    @property
    def getPrecio(self) -> float:
        return self.__precio

    @property
    def getstock(self) -> int:
        return self.__precio

    @property
    def getCategoria(self) -> int:
        return self.__categoria

    @property
    def getTienda(self) -> str:
        return self.__tienda

    @nombre.setter
    def setNombre(self, new_value):
        self.__nombre = new_value
    
    ##SETTER ##
    @descripcion.setter
    def setDescripcion(self, new_value):
        self.__descripcion = new_value

    @precio.setter
    def setPrecio(self, new_value):
        self.__precio = new_value
    
    @stock.setter
    def setStock(self, new_value):
        self.__stock = new_value

    @categoria.setter
    def setCategoria(self, new_value):
        self.__categoria = new_value

    ## GENERERAR CODIGO DE PRODUCTO
    def generarCodigo(self) -> str:
        count = 0
        database = sqlite3.connect("data/linioexp.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            SELECT COUNT(*) FROM productos'''
            cursor.execute(query)
            count = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return "PROD" + "0" * (4 - len(str(count[0] + 1))) + str(count[0] + 1)

    ## AGREGAR NUEVO PRODUCTO
    def agregar_producto(self) -> bool:
        estado_op = False
        database = sqlite3.connect("data/linioexp.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                    INSERT INTO productos(codigo, nombre, descripcion, precio, stock, categoria, tienda)
                    VALUES ('{}', '{}', '{}', {}, {}, {}, '{}')
                    '''.format(self.generarCodigo(), self.__nombre, self.__descripcion,
                            self.__precio, self.__stock, self.__categoria, self.__tienda)
            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op

    ## OBTENER TODOS LOS PRODUCTOS
    def obtenerProductos(self):
        list_product = None
        database = sqlite3.connect("data/linioexp.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            SELECT * FROM producto
            '''
            cursor.execute(query)  # EJECUTA LA OPERACION
            list_product = cursor.fetchall()
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            raise e
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return list_product

    ## OBTENER UN SOLO PRODUCTO POR CODIGO
    def obtenerProducto(self, codigo:str):
        list_product = None
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                SELECT * FROM producto
                WHERE codigo = '{}'
                '''.format(codigo)

            cursor.execute(query)  # EJECUTA LA OPERACION
            list_product = cursor.fetchone()
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            raise e
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return list_product

    ## ACTUALIZAR UN PRODUCTO
    def actualizar_dato(self) -> bool:
        estado_ope: bool = False
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS

        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            UPDATE producto
            SET descripcion = '{}', precio = {}, stock = {}
            WHERE codigo = '{}'
            '''.format(self.__descripcion, self.__precio, self.__stock, self.__codigo)
            cursor.execute(query)  # EJECUTA LA OPERACION
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado_ope = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            raise e
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
        return estado_ope
    
    ## BUSCADOR POR NOMBRE
    def buscarProductoCategoria(self, id_Prod:int):
        lista_productos = None
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                    SELECT *
                    FROM producto
                    WHERE categoria = {}
                    '''.format(id_Prod)
            cursor.execute(query)
            lista_productos = cursor.fetchall()
            return lista_productos
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
            return lista_productos


    ## BUSCADOR POR NOMBRE
    def buscarProducto(self, nombre:str):
        lista_productos = None
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                    SELECT *
                    FROM producto
                    WHERE nombre LIKE '%{}%'
                    '''.format(nombre)
            cursor.execute(query)
            lista_productos = cursor.fetchall()
            return lista_productos
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

    ## ACTUALIZAR STOCK DE UN PRODUCTO
    def actualizarProductoStock(self, id_prod:str) -> bool:
        estado = False
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                UPDATE producto SET stock=stock-1 
                WHERE codigo='{}' '''.format(id_prod)
            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado = True
            return estado
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

    