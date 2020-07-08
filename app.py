# Importación de clases
from functools import wraps
from flask import Flask, render_template, request, redirect, session, g
from models.usuario import Usuario
from models.proveedor import Proveedor
from models.categoria import Categoria
from models.producto import Producto


app = Flask(__name__)

## Instancia  DE CLASES
ClassUsuario    = Usuario()
ClassProveedor  = Proveedor()
ClassCategoria  = Categoria()
ClassProducto   = Producto()

# Ruta de inicio de página
@app.route('/')
def home():
    categorias = ClassCategoria.obtenerCategorias()
    return render_template('home.html', categoriasB = categorias)

#Registro de usuario
@app.route('/registro', methods=["get", "post"])
def registration():
    if request.method == "POST":
        #Capturamos las variables del formulario
        nombres     =   request.form["name"]
        apellidos   =   request.form["lastname"]
        documento   =   request.form["document"]
        email       =   request.form["email"]
        telefono    =   request.form["phone"]
        edad        =   int(request.form["age"])

        username    =   request.form["username"]
        password    =   request.form["password"]
        
        cliente = Usuario(
                nombres         =nombres,
                apellidos       =apellidos,
                documento       =documento,
                edad            =edad,
                email           =email,
                telefono        =telefono,
                username        =username,
                password        =password
            )

        estado_op = cliente.crearUsuario()
        if estado_op:
            return redirect("login")
        else:
            error = 'No se ha podido registrar su cuenta'
            return render_template('users/register.html', error=error)

    return render_template('users/register.html', request=request)

#Registro de proveedor
@app.route('/registrop', methods=["get", "post"])
def registrationP():
    if request.method == "POST":
        #Capturamos las variables del formulario
        nombre      =   request.form["name"]
        direccion   =   request.form["address"]
        ruc         =   request.form["ruc"]
        password    =   request.form["password"]
        
        tienda = Proveedor(
                nombre      =nombre,
                direccion   =direccion,
                ruc         =ruc,
                password    =password
            )
        estado_op = tienda.crearProveedor()
        if estado_op:
            return redirect("loginp")
        else:
            error = 'Revise sus datos'
            return render_template('proveedor/register.html', error=error)

    return render_template('proveedor/register.html', request=request)

#Ruta para logueo de usuarios
@app.route('/login', methods=["get","post"])
def login():
    if request.method == "POST":
        username=request.form["username"]
        user = ClassUsuario.obtenerUsuario(username = username)
        if not user:
            error = 'No se encuentra registrado'
            return render_template('users/login.html', error=error)

        if request.form["password"] == user.password:
            session['user_id'] = user.codigo
            session['user_name'] = user.nombres
            session['user_email'] = user.email
            session['username'] = user.username
            session['type'] = 1
            return redirect("/")
        else:
            error = 'Invalid password'
            return render_template('users/login.html', error=error)

    return render_template('users/login.html')

#Ruta para logueo de comercios
@app.route('/loginp', methods=["get","post"])
def loginP():
    if request.method == "POST":
        ruc=int(request.form["ruc"])
        comercio = ClassProveedor.obtenerProveedor(ruc=ruc)
        if not comercio:
            error = 'No se encuentra registrado'
            return render_template('proveedor/login.html', error=error)

        if request.form["password"] == comercio[4]:
            session['user_ruc'] = comercio[3]
            session['user_nombrep'] = comercio[1]
            session['type'] = 2
            return redirect("/")
        else:
            error = 'Invalid password'
            return render_template('proveedor/login.html', error=error)

    return render_template('proveedor/login.html')

# Funcion solo permitir el ingreso si estas logueado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['user_name'] is None:
            return redirect('login')
        return f(*args, **kwargs)
    return decorated_function

#Cerrar sesion
@app.route('/logout')
@login_required
def logout():
    # Borramos todas las sesiones
    session.clear()
    return redirect("/")

# Funcion solo permitir el ingreso si estas logueado
def login_requiredP(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['user_ruc'] is None:
            return redirect('loginp')
        return f(*args, **kwargs)
    return decorated_function

#Cerrar sesion
@app.route('/logoutP')
@login_requiredP
def logoutP():
    # Borramos todas las sesiones
    session.clear()
    return redirect("/")

#Ruta para Registrar un producto SOLO para Comercios
@app.route('/registroProducto', methods=["get","post"])
@login_requiredP
def registrarProducto():
    categorias = ClassCategoria.obtenerCategorias()
    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = int(request.form["categoria"])
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = int(request.form["stock"])
        nombreProveedor = session['user_nombrep']

        produc = Producto(
            nombre  =nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            tienda=nombreProveedor
        )

        estado_op = produc.agregar_producto()

        if produc:
            return redirect("/")
        else:
            error = 'Verifique los datos'
            return render_template('products/register.html', categoriasB=categorias, error=error)

    return render_template('products/register.html', categoriasB=categorias)

#Ruta para listar productos segun la categoria y buscador segun nombre dentro de la categoria
@app.route('/productoCategoria/<id_categoria>', methods=["get","post"])
def product_category(id_categoria):
    idCategoria = int(id_categoria)
    product_list = ClassProducto.obtenerProductosCategoria(idCategoria)

    if request.method == "POST":
        nombre = request.form["search"]

        product = ClassProducto.buscarProducto(nombre=nombre)

        if not product:
            return render_template("products/category.html",product_list=product, error = "No se ha encontrado su producto")
        else:
            return render_template("products/category.html",product_list=product)

    return render_template("products/category.html",product_list=product_list)

# Mostrar los detalles del producto
@app.route('/producto/<idproducto>',methods=["get"])
def product_detail(idproducto):
    productos= ClassProducto.obtenerProducto(codigo= idproducto)
    return render_template('products/detail.html', productos=productos)



if __name__ == "__main__":
    app.secret_key = "clave_super_ultra_secreta"
    app.run(debug=True)