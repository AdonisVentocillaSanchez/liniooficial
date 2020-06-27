import sqlite3

con = sqlite3.connect('linio.db')
cursor = con.cursor()

#Insertar datos - categoria
cursor.execute("""
INSERT INTO categoria(nombre)
    VALUES ('Arte y artesanias'),
    ('Computadoras'),
    ('Moda'),
    ('Belleza y cuidado personal'),
    ('Salud y Bienestar'),
    ('Deportes'),
    ('Juguetes'), 
    ('Electrodomesticos')
    """)
con.commit()

#Validacion de datos registrados
cursor.execute('SELECT * FROM categoria')
rows = cursor.fetchall()
for row in rows:
    print(row)