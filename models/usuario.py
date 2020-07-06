import sqlite3

class Usuario(object):
    
    def __init__(self, codigo:int=None, nombres:str=None, apellidos:str=None,
                documento:str=None, edad:int=None, email:str=None,
                telefono:int=None, username:str=None,
                password:str=None):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__documento = documento
        self.__edad = edad
        self.__email = email
        self.__telefono = telefono
        self.__username = username
        self.__password = password

    @property
    def password(self) -> str:
        return self.__password

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nombres(self) -> str:
        return self.__nombres

    @property
    def apellidos(self) -> str:
        return self.__apellidos

    @property
    def documento(self) -> str:
        return self.__documento

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def email(self) -> str:
        return self.__email

    @property
    def telefono(self) -> int:
        return self.__telefono

    @property
    def username(self) -> str:
        return self.__username

    @codigo.setter
    def codigo(self, pcodigo):
        self.__codigo = pcodigo

    @apellidos.setter
    def apellidos(self, papellidos):
        self.__apellidos = papellidos

    @edad.setter
    def edad(self, pedad):
        self.__edad = pedad

    @email.setter
    def email(self, pemail):
        self.__email = pemail

    @telefono.setter
    def telefono(self, ptelefono):
        self.__telefono = ptelefono

    @username.setter
    def username(self, pusername):
        self.__username = pusername

    @password.setter
    def password(self, ppassword):
        self.__password = ppassword

    ## CREAR CUENTA
    def crearUsuario(self) -> bool:
        status  = False
        
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            INSERT INTO usuario(nombres, apellidos, documento, edad, email, telefono, username, password)
            VALUES ('{}', '{}', '{}', {}, '{}','{}', '{}', '{}')
            '''.format(self.__nombres, self.__apellidos, self.__documento, self.__edad, self.__email, self.__telefono, self.__username, self.__password)

            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY

            status = True

        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
            return status

    #OBTENER USUARIO
    def obtenerUsuario(self, username:str):
        usuario = None
        try:
            database = sqlite3.connect("data/linio.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                SELECT *
                FROM usuario WHERE username= '{}'
                '''.format(username)

            cursor.execute(query)
            usuario = cursor.fetchone()

            user = Usuario(
                codigo          =usuario[0],
                nombres         =usuario[1],
                apellidos       =usuario[2],
                documento       =usuario[3],
                edad            =usuario[4],
                email           =usuario[5],
                telefono        =usuario[6],
                username        =usuario[7],
                password        =usuario[8]
            )
            return user

        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()
            return usuario