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
    nombres TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    documento TEXT NOT NULL,
    edad INTEGER,
    email TEXT NOT NULL,
    telefono INTEGER,
    username TEXT NOT NULL,
    password TEXT NOT NULL)
    """)
con.commit()

#Creación de tabla Proveedor
cursor.execute("""
DROP TABLE IF EXISTS proveedor;
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS proveedor (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    RUC INTEGER,
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
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio DOUBLE,
    stock INTEGER,
    categoria INTEGER,
    imagen TEXT,
    tienda Integer NOT NULL,
    FOREIGN KEY(categoria) REFERENCES categoria(codigo_categoria),
    FOREIGN KEY(tienda) REFERENCES proveedor(codigo)
    )"""
    )
con.commit()

