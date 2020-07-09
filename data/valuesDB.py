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

#Insertar datos - proveedor
# cursor.execute("""
# INSERT INTO proveedor(nombre, direccion, RUC, password)
#     VALUES ('Arte y artesanias'),
#     ('Computadoras'),
#     ('Moda'),
#     ('Belleza y cuidado personal'),
#     ('Salud y Bienestar'),
#     ('Deportes'),
#     ('Juguetes'), 
#     ('Electrodomesticos')
#     """)
# con.commit()

# #Validacion de datos registrados
# cursor.execute('SELECT * FROM proveedor')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

#Insertar datos - producto
# cursor.execute("""
# INSERT INTO producto(codigo, nombre, descripcion, precio, stock, categoria, tienda )
#     VALUES 
#     ('PROD0001', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0002', 'Play Station 4 Slim - Negro - 1 TB', 'Consola más fina y ligera con un estilizado nuevo diseño que encierra una potente PlayStation®4 en su interior. 30% más delgada y un 16% más ligera que 
#     su antecesora. Pero que no te engañe su compacto diseño, su interior alberga un disco duro de 1TB de capacidad.Disfruta del HDR también en tu consola favorita. Las imágenes son más realistas, impactantes, vívidas. 
#     Es como si vieras a través de una ventana, lo más parecido a lo que un ojo humano es capaz de ver en el mundo real. Lo disfrutarás al máximo no sólo en los juegos sino también en todas las aplicaciones de cine, 
#     tele y mucho más a las que puedes acceder. Mejoras e innovaciones para el juego como los modos Remote Play y el Share Play. El modo Remote Play te permite jugar a tus juegos en otros dispositivos mediante WiFi, como por ejemplo, en tu PS Vita.',
#     1099, 50, 6, 'Mi tienda' ),
#     ('PROD0003', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0004', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0005', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0006', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0007', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0008', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0009', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' ),
#     ('PROD0010', 'GoPro Hero 7 4K UHD - Black', 'Estabilización Superfluido de video: Consigue estabilización sin tener que usar instrumentos. La HERO7 Black prevé tus movimientos y los corrige,
#     lo que evita vibraciones de la cámara y ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no puedes capturar con tu teléfono. La HERO7 Black es resistente
#     y sumergible sin carcasa hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento. Controla tu HERO7 Black sin tener que usar las manos mediante comandos de voz 
#     como GoPro toma una foto y GoPro graba video. Video en 4K y 60 fps, y fotos de 12 MP: La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los propios momentos. 
#     Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a 240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo su esplendor.',
#     1199, 50, 6, 'Mi tienda' )
#     """)
# con.commit()

# #Validacion de datos registrados
# cursor.execute('SELECT * FROM producto')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)