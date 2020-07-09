# Importación de clases
from functools import wraps
from flask import Flask, render_template, request, redirect, make_response, url_for, session, g
import json
from models.usuario import Usuario
from models.proveedor import Proveedor
from models.categoria import Categoria
from models.producto import Producto
from models.pedido import Pedido
# Importacion de clases para manejar archivos (imagenes)
import os
from werkzeug.utils import secure_filename
## Importación fechas
from datetime import datetime as dt
## Importacion Culqi
import culqipy



app = Flask(__name__)
## DEFINIMOS RUTA DONDE SE SUBIRAN LOS ARCHIVOS
app.config['UPLOAD_FOLDER'] = "./static"

## Instancia  DE CLASES
ClassUsuario    = Usuario()
ClassProveedor  = Proveedor()
ClassCategoria  = Categoria()
ClassProducto   = Producto()
ClassPedido     = Pedido()

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
            session['user_id'] = comercio[0]
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
        idProveedor = session['user_id']
        ## GUARDAMOS LA IMAGEN
        imagen = request.files['imagen']
        archivoImagen = secure_filename(imagen.filename)
        imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], archivoImagen))
        

        produc = Producto(
            nombre  =nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            imagen=archivoImagen,
            tienda=idProveedor
        )

        estado_op = produc.agregar_producto()

        if estado_op:
            msg = "Producto registrado"
            return render_template('products/register.html', categoriasB=categorias, error=msg)
        else:
            error = 'Verifique los datos'
            return render_template('products/register.html', categoriasB=categorias, error=error)

    return render_template('products/register.html', categoriasB=categorias)

# Listar producto proveedor
@app.route('/listarproducto')
@login_requiredP
def listarproducto():
    idTienda = int(session['user_id'])
    productos= ClassProducto.obtenerProductosTienda(idtienda=idTienda)
    return render_template('products/list.html', product_list=productos)

# actualizar producto proveedor
@app.route('/modificarproducto/<idproducto>',methods=["get","post"])
@login_requiredP
def product_modify(idproducto):
    productoMod = ClassProducto.obtenerProducto(codigo=idproducto)
    if not productoMod:
        msg = "Verifique codigo del producto"
        return render_template('products/modify.html', error=msg)
    categorias = ClassCategoria.obtenerCategorias()    
    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = int(request.form["categoria"])
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = int(request.form["stock"])
        producNew = Producto(
            codigo= idproducto,
            nombre  =nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria
        )

        estado_op = producNew.actualizarProducto()

        if estado_op:
            msg = "Producto actualizado"
            return render_template('products/modify.html', msg=msg)
        else:
            error = 'Verifique los datos'
            return render_template('products/modify.html', categoriasB=categorias, error=error)
    return render_template('products/modify.html', categoriasB=categorias, productoMod=productoMod)

# eliminar producto proveedor
@app.route('/eliminarproducto/<idproducto>',methods=["get"])
@login_requiredP
def product_delete(idproducto):
    eliminar = ClassProducto.eliminarProducto(id_prod=idproducto)
    if eliminar:
        msg = "Producto Eliminado"
        return render_template('products/list.html', msg=msg)
    else:
        msg = "Producto Eliminado"
        return render_template('products/list.html', msg=msg)

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

@app.route('/Bproducto', methods=["get","post"])
def search_producto():
    if request.method == "POST":
        nombre = request.form["search"]

        product = ClassProducto.buscarProducto(nombre=nombre)

        if not product:
            return render_template("products/category.html")
        else:
            return render_template("products/category.html",product_list=product)

    return render_template("products/category.html")

# Mostrar los detalles del producto
@app.route('/producto/<idproducto>',methods=["get"])
def product_detail(idproducto):
    productos= ClassProducto.obtenerProducto(codigo= idproducto)
    return render_template('products/detail.html', productos=productos)
    

########### CARRITO

## VER MIS COMPRAS
@app.route('/compras')
@login_required
def view_compras():
    idusu = session['user_id']
    mispedidos = ClassPedido.obtenerPedidosUsuario(iduser=idusu)
    if mispedidos:
        return render_template('carts/view.html', mispedidos = mispedidos)
    else:
        msg = "No tienes compras registradas"
        return render_template('carts/view.html', msg=msg)

@app.route('/cancelarPedido/<id_ped>')
@login_required
def cancelar_pedido(id_ped):
    mispedidos = ClassPedido.cancelarPedido(idpedido=id_ped)
    if mispedidos:
        msg = "Se ha cancelado tu pedido"
        return render_template('carts/view.html', msg=msg)
    else:
        msg = "No se ha podido cancelar tu pedido"
        return render_template('carts/view.html', msg=msg)

## VER CARRITO
@app.route('/carrito')
@login_required
def view_carrito():
    return render_template('carts/list.html')


## AGREGAR PRODUCTO A CARRITO
@app.route('/addcarrito/<idproducto>')
@login_required
def add_carrito(idproducto):
    productAdd = ClassProducto.obtenerProducto(codigo=idproducto)
    itemArray =[(
        productAdd[0],productAdd[1],productAdd[3]
    )]
    if 'product_list' and 'precio_total' in session:
        session['product_list'] = session['product_list']+itemArray
        session['precio_total'] = session['precio_total']+productAdd[3]
    else:
         session['product_list'] = itemArray
         session['precio_total'] = productAdd[3]

    return render_template('products/category.html')

##BORRAR CARRITO
@app.route('/borrarcarrito')
def empty_cart():
    if 'product_list' and 'precio_total' in session:
        session.pop('product_list',None)
        session.pop('precio_total',None)
        msg = "Se eliminó el carrito"
        return render_template('carts/view.html', msg=msg)
    else:
        msg = "Error"
        return render_template('carts/view.html', msg=msg)


## PAGAR CARRITO
@app.route('/pagarcarrito', methods=["get", "post"])
@login_required
def pagar_carrito():
    if request.method == "POST":
        provincia = request.form["provincia"]
        distrito = request.form["distrito"]
        direccion = request.form["direccion"]
        dir_envio = provincia+" / "+distrito+" / "+direccion
        comprobante = request.form["comprobante"]
        paytoken = request.form["paytoken"]
        payamount = request.form["payamount"]

        status = "Pagado"

        ## Capturamos la fecha 
        now1 = dt.now()
        fecha = now1.strftime('%Y-%m-%d %H:%M:%S')

        carritoNew = Pedido(
            codigo_usuario= int(session['user_id']),
            estado= status,
            tipo_comprobante= comprobante,
            hashCulqi= paytoken,
            direccion_envio= dir_envio,
            pago=payamount,
            fecha_emision=fecha
        )

        crearCarrito = carritoNew.agregarPedido()

        if crearCarrito:
            session.pop('product_list',None)
            session.pop('precio_total',None)
            msg = "Se ha registrado tu compra"
            return render_template('carts/view.html', msg=msg)
        else:
            error = 'Hubo un error al procesar la compra'
            return render_template('carts/view.html', error=error)
    return render_template('carts/list.html')


## Funcion para unir arrays (carrito)
def unir_array( lista1 , lista2 ):
    if isinstance( lista1 , list ) and isinstance( lista2 , list ):
        return lista1 + lista2
    elif isinstance( lista1 , dict ) and isinstance( lista2 , dict ):
        return dict( list( lista1.items() ) + list( lista2.items() ) )
    elif isinstance( lista1 , set ) and isinstance( lista2 , set ):
        return lista1.union( lista2 )
    return False

if __name__ == "__main__":
    app.secret_key = "clave_super_ultra_secreta"
    app.run(debug=True)