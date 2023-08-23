from django.contrib import admin

from gestionTLV.models import Clientes, Productos, Pedidos, RelacionPedidosProductos

class ClientesAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 
            'nombre_cliente', 
            'apellidos_cliente', 
            'direccion_cliente', 
            'ciudad_cliente', 
            'comuna_cliente', 
            'sector_cliente',
            'telefono_cliente', 
            'correo_cliente',
            'password_cliente',
            'crea_cliente']
    
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['id_producto', 
            'nombre_producto', 
            'marca_producto', 
            'unidad_producto', 
            'categoria_producto', 
            'stock_producto', 
            'precio_producto']

class PedidosAdmin(admin.ModelAdmin):
    list_display = ['id_pedido', 
            'id_cliente', 
            'fecha_pedido', 
            'fecha_entrega', 
            'estado_pedido',
            'forma_pago']

class RelacionPedidosProductosAdmin(admin.ModelAdmin):
    list_display = ['id_pedido', 'id_producto', 'cantidad_pedido']

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(RelacionPedidosProductos, RelacionPedidosProductosAdmin)