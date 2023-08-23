from django import forms
from .models import Clientes, Productos, Pedidos, RelacionPedidosProductos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

##################### APLICACIÓN ##########################
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['id_cliente', 
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

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id_producto', 
            'nombre_producto', 
            'marca_producto', 
            'unidad_producto', 
            'categoria_producto', 
            'stock_producto', 
            'precio_producto']

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['id_pedido', 
            'id_cliente', 
            'fecha_pedido', 
            'fecha_entrega', 
            'estado_pedido',
            'forma_pago']

class RelacionPedidosProductosForm(forms.ModelForm):
    class Meta:
        model = RelacionPedidosProductos
        fields = ['id_pedido', 'id_producto', 'cantidad_pedido']


##################### USERS ##########################

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True, 
        label="Nombre de usuario", 
        error_messages={'required': 'Su nombre es requerido'})
    password = forms.CharField(widget=forms.PasswordInput, 
        max_length=20, required=True, 
        label="Contraseña", 
        error_messages={'required': 'Contraseña es obligatoria'})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'password1', 'password2']