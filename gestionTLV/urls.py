
from django.contrib import admin
from django.urls import path
from gestionTLV.views import gestionTLV
from gestionTLV.views import *
from gestionTLV.views import user_login, registro
from django.contrib.auth import views

urlpatterns = [
    #path('admin/', admin.site.urls),  
    #path('comercial/', vista_comercial, name='vista_comercial'),
    path('', gestionTLV, name = 'index'),
    path('registro_clientes/login/', gestionTLV, name = 'index'),
    path('administra_clientes/login/', gestionTLV, name = 'index'),
    path('registro_clientes/', registroClientes, name = 'registro_clientes'),
    path('administra_clientes/', administraClientes, name = 'administra_clientes'),
    path('modifica_clientes/<id_cliente>/', modificaClientes, name="modifica_clientes"),
    path('elimina_clientes/<id_cliente>/', eliminaClientes, name = 'elimina_clientes'),
    #path('login_clientes/', loginClientes, name = 'login_clientes'),


    path('registro_productos/login/', gestionTLV, name = 'index'),
    path('administra_productos/login/', gestionTLV, name = 'index'),
    path('registro_productos/', registroProductos, name = 'registro_productos'),
    path('administra_productos/', administraProductos, name = 'administra_productos'),
    path('modifica_productos/<id_producto>/', modificaProductos, name="modifica_productos"),
    path('elimina_productos/<id_producto>/', eliminaProductos, name = 'elimina_productos'),

    path('registro_pedidos/login/', gestionTLV, name = 'index'),
    path('administra_pedidos/login/', gestionTLV, name = 'index'),
    path('registro_pedidos/', registroPedidos, name = 'registro_pedidos'),
    path('administra_pedidos/', administraPedidos, name = 'administra_pedidos'),
    path('modifica_pedidos/<id_pedido>/', modificaPedidos, name="modifica_pedidos"),
    path('elimina_pedidos/<id_pedido>/', eliminaPedidos, name = 'elimina_pedidos'),
    path('cambiaEstado_pedidos1/<id_pedido>/', cambiaEstadoPedidos1, name = 'cambiaEstado_pedidos1'),
    path('cambiaEstado_pedidos2/<id_pedido>/', cambiaEstadoPedidos2, name = 'cambiaEstado_pedidos2'),
    path('cambiaEstado_pedidos3/<id_pedido>/', cambiaEstadoPedidos3, name = 'cambiaEstado_pedidos3'),
    path('cambiaEstado_pedidos4/<id_pedido>/', cambiaEstadoPedidos4, name = 'cambiaEstado_pedidos4'),

    path('registro_detalle/login/', gestionTLV, name = 'index'),
    path('administra_detalle/login/', gestionTLV, name = 'index'),
    path('registro_detalle/', registroDetalle, name = 'registro_detalle'),
    path('administra_detalle/', administraDetalle, name = 'administra_detalle'),
    path('modifica_detalle/<pedido>/', modificaDetalle, name="modifica_detalle"),
    path('elimina_detalle/<pedido>/', eliminaDetalle, name = 'elimina_detalle'),

    path('administra_detalle_pedido/<pedido>/', administraDetallePedido, name='administra_detalle_pedido'),

    path('contactar1/<str:id_cliente>/', contactar1, name = 'contactar1'),
    path('contactar2/<str:id_cliente>/', contactar2, name = 'contactar2'),
    path('contactar3/<str:id_cliente>/', contactar2, name = 'contactar3'),
    path('contactar4/<str:id_cliente>/', contactar3, name = 'contactar4'),

    path('login/', user_login, name = 'login'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('registro/', registro, name='registro')
    
]
