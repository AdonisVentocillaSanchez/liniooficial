# Importación de clases
from functools import wraps
from flask import Flask, render_template, request, redirect, session, g
from models.Usuario import Usuario
from models.proveedor import Proveedor
from models.categoria import Categoria
from models.producto import Producto


app = Flask(__name__)

## IMPORTACION DE CLASES
ClassUsuario    = Usuario()
ClassProveedor  = Proveedor()
ClassCategoria  = Categoria()
ClassProducto   = Producto()

# Ruta de inicio de página
@app.route('/')
def home():
    categorias = ClassCategoria.obtenerCategorias()
    return render_template('home.html', categorias = categorias)

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
        tarjeta     =   int(request.form["tarjeta"])
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
                tarjeta_banco   =tarjeta,
                username        =username,
                password        =password
            )

        estado_op = cliente.crearUsuario()
        if estado_op:
            return redirect("login")
        else:
            error = 'Invalid email'
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
            error = 'Invalid email'
            return render_template('proveedor/register.html', error=error)

    return render_template('proveedor/register.html', request=request)

#Ruta para logueo de usuarios
@app.route('/login', methods=["get","post"])
def login():
    if request.method == "POST":
        username=request.form["username"]
        user = ClassUsuario.obtenerUsuario(username = username)

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
        ruc=request.form["ruc"]
        comercio = ClassProveedor.obtenerProveedor(ruc=ruc)

        if request.form["password"] == comercio.contrasena:
            session['user_name'] = comercio.ruc
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
            return redirect('inicio-sesion')
        return f(*args, **kwargs)
    return decorated_function

#Cerrar sesion
@app.route('/logout')
@login_required
def logout():
    session['user_name'] = None
    session['user_email'] = None
    return redirect("/")

#Ruta para listar productos segun la categoria y buscador segun nombre dentro de la categoria
@app.route('/productoCategoria/<id_categoria>', methods=["get","post"])
def product_category(id_categoria):
    idCategoria = int(id_categoria)
    product_list = ClassProducto.buscarProductoCategoria(idCategoria)

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
    productos= Producto.obtenerProducto(codigo= idproducto)
    return render_template('products/detail.html', productos=productos)



if __name__ == "__main__":
    app.secret_key = "clave_super_ultra_secreta"

    app.run(debug=True)