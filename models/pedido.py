import sqlite3

class Pedido(object):
    def __init__(self, codigo:int=None, codigo_usuario:int=None, estado:str=None, tipo_comprobante:str=None
                , hashCulqi:str=None, direccion_envio:str=None, pago:int=None, fecha_emision:str=None):
        self.codigo = codigo
        self.codigo_usuario = codigo_usuario
        self.estado = estado
        self.tipo_comprobante = tipo_comprobante
        self.hashCulqi = hashCulqi
        self.direccion_envio = direccion_envio
        self.pago = pago
        self.fecha_emision = fecha_emision

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, pcodigo):
        self.__codigo = pcodigo

    @property
    def codigo_usuario(self):
        return self.__codigo_usuario
    @codigo_usuario.setter
    def codigo_usuario(self, value):
        self.__codigo_usuario = value

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, value):
        self.__estado = value
    
    @property
    def tipo_comprobante(self):
        return self.__tipo_comprobante
    @tipo_comprobante.setter
    def tipo_comprobante(self, value):
        self.__tipo_comprobante = value

    @property
    def hashCulqi(self):
        return self.__hashCulqi
    @hashCulqi.setter
    def hashCulqi(self, value):
        self.__hashCulqi = value

    @property
    def direccion_envio(self):
        return self.__direccion_envio
    @direccion_envio.setter
    def direccion_envio(self, value):
        self.__direccion_envio = value

    @property
    def pago(self):
        return self.__pago
    @pago.setter
    def pago(self, value):
        self.__pago = value

    @property
    def fecha_emision(self):
        return self.__fecha_emision
    @fecha_emision.setter
    def fecha_emision(self, value):
        self.__fecha_emision = value

    ## OBTENER PEDIDOS
    def obtenerPedidos(self):
        dato=None
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                SELECT *
                FROM pedido
                '''
            cursor.execute(query)
            dato = cursor.fetchall()
            return dato

        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()
        return dato
    
    ## OBTENER PEDIDOS de usuario
    def obtenerPedidosUsuario(self, iduser:int):
        dato=None
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                SELECT *
                FROM pedido where codigo_usuario={}
                '''.format(iduser)
            cursor.execute(query)
            dato = cursor.fetchall()
            return dato

        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()
        return dato

    ## OBTENER PEDIDOS de usuario
    def cancelarPedido(self, idpedido:int):
        dato=False
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                UPDATE pedido SET estado='cancelado'
                where codigo={}
                '''.format(idpedido)
            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            dato = True
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()
        return dato

    ## AGREGAR PEDIDO
    def agregarPedido(self) -> bool:
        estado_op = False
        database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                    INSERT INTO pedido(codigo_usuario, estado, tipo_comprobante, hashCulqi, direccion_envio, pago, fecha_emision)
                    VALUES ({}, '{}', '{}', '{}', '{}', {}, '{}')
                    '''.format( self.__codigo_usuario, self.__estado, self.__tipo_comprobante, self.__hashCulqi, self.direccion_envio, self.pago, self.__fecha_emision)
            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
        return estado_op