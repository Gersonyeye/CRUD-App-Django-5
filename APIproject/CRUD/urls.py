from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Crear usuario/', views.usuarioFormView, name='create_url'),
    path('usuarios/', views.listaView, name='lista_url'),
    path('actualizar/<int:f_cedula>', views.updateView, name= 'update_url'),
    path('eliminar/<int:f_cedula>', views.deleteView, name= 'delete_url'),
    path('logout/', views.exit, name='exit'),
    
]