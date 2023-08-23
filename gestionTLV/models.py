from django.db import models
from datetime import datetime, date
from django.utils import timezone

categorias = (
    ("1", "Zapatillas deportivas"),
    ("2", "Zapatillas urbanas"),
    ("3", "Ropa deportiva"),
    ("4", "Implementos deportivos"),
    ("5", "Máquinas de ejercicios"),
    ("6", "Otras categorías"),
)

estados = (
    ("1", "Pendiente"),
    ("2", "En preparación"),
    ("3", "En despacho"),
    ("4", "Entregado"),
)

formas_de_pago = (
    ("1", "Contado, T.Debito"),
    ("2", "Por T.Crédito 1 cuota"),
    ("3", "Por T.Crédito 3 cuotas"),
    ("4", "Por T.Crédito 6 cuotas"),
    ("5", "Por T.Crédito 12 cuotas"),
    ("6", "Por T.Crédito 24 cuotas"),
)

class Clientes(models.Model):
    id_cliente = models.CharField(
        null= False,
        max_length = 6,
        primary_key = True,
        default = '999999'
        )   
    nombre_cliente = models.CharField(max_length=30)
    apellidos_cliente = models.CharField(max_length=30)
    direccion_cliente = models.CharField(max_length=60)
    ciudad_cliente = models.CharField(max_length=30)
    comuna_cliente = models.CharField(max_length=30)
    sector_cliente = models.CharField(max_length=30)
    telefono_cliente = models.CharField(max_length=12)
    correo_cliente = models.EmailField(max_length=40)
    password_cliente = models.CharField(max_length=8)  
    crea_cliente = models.DateField(default=timezone.now)

    def __str__(self):
        return "Id: %s, Nombre: %s, Apellidos: %s,  Dirección: %s, Ciudad: %s, Comuna: %s, Sector: %s, Teléfono: %s, Correo: %s, Password: %s, Creación: %s" %(
            self.id_cliente, 
            self.nombre_cliente, 
            self.apellidos_cliente, 
            self.direccion_cliente, 
            self.ciudad_cliente, 
            self.comuna_cliente, 
            self.sector_cliente,
            self.telefono_cliente, 
            self.correo_cliente,
            self.password_cliente,
            self.crea_cliente)
    

class Pedidos(models.Model):
    id_pedido = models.IntegerField(
        null= False,
        primary_key = True,
        auto_created= True,
        )               
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    fecha_entrega = models.DateTimeField(default=timezone.now)
    estado_pedido = models.CharField(max_length=1, choices=estados, default='1')
    forma_pago = models.CharField(max_length=1, choices=formas_de_pago, default='1')
                          
    def __str__(self):
        return "Id: %s, id-cliente: %s, Fecha pedido: %s,  Fecha entrega: %s, Estado: %s, Forma de pago: %s" %(
            self.id_pedido, 
            self.id_cliente, 
            self.fecha_pedido, 
            self.fecha_entrega, 
            self.estado_pedido,
            self.forma_pago)
    


class Productos(models.Model):
    id_producto = models.CharField(
        null= False,
        max_length = 6,
        primary_key = True,
        default = '100000'
        )   
    nombre_producto = models.CharField(max_length=60)
    marca_producto = models.CharField(max_length=30)
    unidad_producto = models.CharField(max_length=20)
    categoria_producto = models.CharField(max_length=1, choices=categorias, default='1')
    stock_producto = models.IntegerField() 
    precio_producto = models.IntegerField()  

    def __str__(self):
        return "Id: %s, Nombre: %s, Marca: %s,  Unidad: %s, Categoria: %s, Stock: %s, Precio: %s" %(
            self.id_producto, 
            self.nombre_producto, 
            self.marca_producto, 
            self.unidad_producto, 
            self.categoria_producto, 
            self.stock_producto, 
            self.precio_producto)
    


class RelacionPedidosProductos(models.Model):
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_pedido = models.IntegerField()

    def __str__(self):
        return self.id_pedido, self.id_producto, self.cantidad_pedido
    


