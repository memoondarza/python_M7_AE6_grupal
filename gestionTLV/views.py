from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from gestionTLV.models import *
from .forms import ClientesForm, ProductosForm, PedidosForm, RelacionPedidosProductosForm, LoginForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context



def gestionTLV(request):
    return render(request, 'landing.html')

#################### CLIENTES ################################################################
@login_required
def registroClientes(request):
    data = {
        'form': ClientesForm()
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "CLIENTE REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro_clientes.html', data)

@login_required
def administraClientes(request):
    clientes = Clientes.objects.all().order_by('id_cliente')
    return render(request, 'administra_clientes.html', {'clientes': clientes})

@login_required
def modificaClientes(request, id_cliente):
    cliente = Clientes.objects.get(pk = id_cliente) 
    data = {
        'form': ClientesForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "CLIENTE ACTUALIZADO !!!"
            return redirect(to='administra_clientes')
        else:
            data["form"] = formulario
    return render(request, 'modifica_clientes.html', data)

@login_required
def eliminaClientes(request, id_cliente):
    cliente_elimina = Clientes.objects.get(pk = id_cliente)
    cliente_elimina.delete()
    return render(request, 'elimina_clientes.html', {'cliente': id_cliente})

"""
@login_required
def loginClientes(request):
    data = {
        'form': ClientesForm()
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "CLIENTE VALIDADO !!!"
           
    return render(request, 'login_clientes.html', {'form': formulario}) 
"""
############################### FIN CLIENTES #############################################

############################### PRODUCTOS #############################################
@login_required
def registroProductos(request):
    data = {
        'form': ProductosForm()
    }
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "PRODUCTO REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro_productos.html', data)

@login_required
def administraProductos(request):
    productos = Productos.objects.all().order_by('id_producto')
    return render(request, 'administra_productos.html', {'productos': productos})

@login_required
def modificaProductos(request, id_producto):
    producto = Productos.objects.get(pk = id_producto) 
    data = {
        'form': ProductosForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "PRODUCTO MODIFICADO !!!"
            return redirect(to='administra_productos')
        else:
            data["form"] = formulario
    return render(request, 'modifica_productos.html', data)

@login_required
def eliminaProductos(request, id_producto):
    producto_elimina = Productos.objects.get(pk = id_producto)
    prod_nombre = producto_elimina.nombre_producto
    producto_elimina.delete()
    return render(request, 'elimina_productos.html', {'producto': prod_nombre})

################################## FIN PRODUCTOS ###################################################

##############################################################################################

################################## PEDIDOS ###################################################

@login_required
def registroPedidos(request):
    data = {
        'form': PedidosForm()
    }
    if request.method == 'POST':
        formulario = PedidosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "PEDIDO REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro_pedidos.html', data)

@login_required
def administraPedidos(request):
    pedidos = Pedidos.objects.all().order_by('id_pedido')
    return render(request, 'administra_pedidos.html', {'pedidos': pedidos})

@login_required
def modificaPedidos(request, id_pedido):
    pedido = Pedidos.objects.get(pk = id_pedido) 
    data = {
        'form': PedidosForm(instance=pedido)
    }
    if request.method == 'POST':
        formulario = PedidosForm(data=request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "PEDIDO MODIFICADO !!!"
            return redirect(to='administra_pedidos')
        else:
            data["form"] = formulario
    return render(request, 'modifica_pedidos.html', data)

@login_required
def eliminaPedidos(request, id_pedido):
    pedido_elimina = Pedidos.objects.get(pk = id_pedido)
    pedido_elimina.delete()
    return render(request, 'elimina_pedidos.html', {'pedido': id_pedido})



@login_required
def cambiaEstadoPedidos1(request, id_pedido):
    pedido_a_cambiar = Pedidos.objects.get(pk = id_pedido)
    obtiene_cliente = pedido_a_cambiar.id_cliente
    pedido_a_cambiar.estado_pedido = "1"
    pedido_a_cambiar.save()
    pedidos = Pedidos.objects.all().order_by('estado_pedido')  
    return render(request, 'contactar1.html', {'id': obtiene_cliente.id_cliente})

@login_required
def cambiaEstadoPedidos2(request, id_pedido):
    pedido_a_cambiar = Pedidos.objects.get(pk = id_pedido)
    obtiene_cliente = pedido_a_cambiar.id_cliente
    pedido_a_cambiar.estado_pedido = "2"
    pedido_a_cambiar.save()
    pedidos = Pedidos.objects.all().order_by('estado_pedido')
    return render(request, 'contactar2.html', {'id': obtiene_cliente.id_cliente})

@login_required
def cambiaEstadoPedidos3(request, id_pedido):
    pedido_a_cambiar = Pedidos.objects.get(pk = id_pedido)
    obtiene_cliente = pedido_a_cambiar.id_cliente
    pedido_a_cambiar.estado_pedido = "3"
    pedido_a_cambiar.save()
    pedidos = Pedidos.objects.all().order_by('estado_pedido') 
    return render(request, 'contactar3.html', {'id': obtiene_cliente.id_cliente})

@login_required
def cambiaEstadoPedidos4(request, id_pedido):
    pedido_a_cambiar = Pedidos.objects.get(pk = id_pedido)
    obtiene_cliente = pedido_a_cambiar.id_cliente
    pedido_a_cambiar.estado_pedido = "4"
    pedido_a_cambiar.save()
    pedidos = Pedidos.objects.all().order_by('estado_pedido')   
    return render(request, 'contactar4.html', {'id': obtiene_cliente.id_cliente})


##############################################################################################


##############################################################################################

################################## DETALLE PEDIDOS ###################################################

@login_required
def registroDetalle(request):
    data = {
        'form': RelacionPedidosProductosForm()
    }
    if request.method == 'POST':
        formulario = RelacionPedidosProductosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "DETALLE PEDIDO REGISTRADO !!!"           
        else:
            data["form"] = formulario
    return render(request, 'registro_detalle.html', data)

@login_required
def administraDetalle(request):
    detalle = RelacionPedidosProductos.objects.all().order_by('id_pedido')
    largo = RelacionPedidosProductos.objects.all().order_by('id_pedido').count()
    precio_parcial = []
    for i in range(0, largo):
        parcial = int(detalle[i].id_producto.precio_producto) * int(detalle[i].cantidad_pedido)
        precio_parcial.append(parcial)
    return render(request, 'administra_detalle.html', {'detalle': detalle, 'pt': precio_parcial})

@login_required
def administraDetallePedido(request, pedido):
    detalle_pedido = RelacionPedidosProductos.objects.filter(id_pedido_id=pedido).order_by('id_pedido')
    largo = RelacionPedidosProductos.objects.filter(id_pedido_id=pedido).order_by('id_pedido').count()
    precio_parcial = []
    total = 0
    for i in range(0, largo):
        parcial = int(detalle_pedido[i].id_producto.precio_producto) * int(detalle_pedido[i].cantidad_pedido)
        precio_parcial.append(parcial)
        total = total + parcial   
    return render(request, 'administra_detalle_pedido.html', {'detalle_pedido': detalle_pedido, 'pt': precio_parcial, 'ptotal': "{:,}".format(total).replace(',','.')})

@login_required
def modificaDetalle(request, pedido):
    detalle = RelacionPedidosProductos.objects.get(pk=pedido)
    data = {
        'form': RelacionPedidosProductosForm(instance=detalle)
    }
    if request.method == 'POST':
        formulario = RelacionPedidosProductosForm(data=request.POST, instance=detalle)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "DETALLE PEDIDO MODIFICADO !!!"
            return redirect(to='administra_detalle')
        else:
            data["form"] = formulario
    return render(request, 'modifica_detalle.html', data)

@login_required
def eliminaDetalle(request, pedido):
    detalle_elimina = RelacionPedidosProductos.objects.get(pk = pedido)
    detalle_elimina.delete()
    return render(request, 'elimina_detalle.html', {'detalle': pedido})

################################## FIN DETALLE PEDIDOS #######################################

#############################################################################################

################################## ENVÍA CORREOS #######################################

@login_required
def contactar1(request, id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    correo = cliente.correo_cliente
    asunto = "Cambió estado de su pedido "
    mensaje = "El estado de su pedido a cambiado a Pendiente"
    email_desde = settings.EMAIL_HOST_USER
    email_para = [correo]
    send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)    
    return render(request, 'administra_pedidos.html')

@login_required
def contactar2(request, id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    correo = cliente.correo_cliente
    asunto = "Cambió estado de su pedido "
    mensaje = "El estado de su pedido a cambiado a En preparación"
    email_desde = settings.EMAIL_HOST_USER
    email_para = [correo]
    send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)    
    return render(request, 'administra_pedidos.html')

@login_required
def contactar3(request, id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    correo = cliente.correo_cliente
    asunto = "Cambió estado de su pedido "
    mensaje = "El estado de su pedido a cambiado a En Despacho"
    email_desde = settings.EMAIL_HOST_USER
    email_para = [correo]
    send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)    
    return render(request, 'administra_pedidos.html')

@login_required
def contactar4(request, id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    correo = cliente.correo_cliente
    asunto = "Cambió estado de su pedido"
    mensaje = "El estado de su pedido a cambiado a Entregado"
    email_desde = settings.EMAIL_HOST_USER
    email_para = [correo]
    send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)    
    return render(request, 'administra_pedidos.html')

################################## FIN ENVÍA CORREOS #######################################




################################### USUARIOS #################################################
def user_login(request):    
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
           usuario = formulario.cleaned_data['usuario']
           password = formulario.cleaned_data['password']
           user = authenticate(request, username=usuario, password=password)
           if user is not None:
               if user.is_active:
                   login(request, user)
                   return render(request, 'registration/bienvenida.html', {'users': usuario})
               else:
                   messages.error(request, "Cuenta no habilitada")
           else:
                messages.error(request, "Login no válido")
    else:
        formulario = LoginForm()
    return render(request, 'registration/login.html', {'formulario': formulario})


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }   
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           usuario = formulario.cleaned_data['username']
           password = formulario.cleaned_data['password1']
           user = authenticate(request, username=usuario, password=password)  
           login(request, user)
           messages.success(request, f"Te has registrado correctamente, estimado(a) {usuario}")   
           return render(request, 'registration/bienvenida.html', {'users': usuario})
                   
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)
