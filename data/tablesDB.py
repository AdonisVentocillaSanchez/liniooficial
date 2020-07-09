import sqlite3

#Conexión con la base de datos
con = sqlite3.connect("linio.db")

cursor =  con.cursor()

#Creación de tabla Usuario
cursor.execute("""
DROP TABLE IF EXISTS usuario;
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombres TEXT(30) NOT NULL,
    apellidos TEXT(30) NOT NULL,
    documento TEXT(10) NOT NULL,
    edad INTEGER(2),
    email TEXT(30) NOT NULL,
    telefono INTEGER(10),
    username TEXT(30) NOT NULL,
    password TEXT(30) NOT NULL)
    """)
con.commit()

#Creación de tabla Proveedor
cursor.execute("""
DROP TABLE IF EXISTS proveedor;
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS proveedor (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT(50) NOT NULL,
    direccion TEXT(50) NOT NULL,
    RUC INTEGER(11),
    password TEXT NOT NULL)
    """)
con.commit()

#Creación de tabla Categoría
cursor.execute("""
DROP TABLE IF EXISTS categoria;
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS categoria (
    codigo INTEGER PRIMARY KEY,
    nombre STRING)
    """)
con.commit()

#Creación de tabla Producto
cursor.execute("""
DROP TABLE IF EXISTS producto;
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS producto (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio DOUBLE,
    stock INTEGER,
    categoria INTEGER,
    imagen TEXT,
    tienda Integer NOT NULL,
    FOREIGN KEY(categoria) REFERENCES categoria(codigo),
    FOREIGN KEY(tienda) REFERENCES proveedor(codigo)
    )"""
    )
con.commit()

#Creación de tabla Producto
cursor.execute("""
DROP TABLE IF EXISTS pedido;
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedido (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_usuario INTEGER,
    estado STRING,
    tipo_comprobante STRING,
    hashCulqi STRING,
    direccion_envio STRING,
    pago DOUBLE,
    fecha_emision DATETIME NOT NULL,
    FOREIGN KEY(codigo_usuario) REFERENCES usuario(codigo))""")
con.commit()