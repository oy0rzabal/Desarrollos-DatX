from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios


TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")

# # usuarios vista:
# def clientes(request):
#     Nombre
#         Apellido
#       Correo
#               >Telefono
#               Fecha de Nacimiento
#              Fecha de Registro
#     datos = { 'usuarios' : users}
#     return render(request, "/usuario.html")

def clientes(request):
    return render(request, "crud_usuarios/clientes.html")