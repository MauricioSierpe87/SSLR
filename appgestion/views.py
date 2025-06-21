from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroSeguroForm
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm
from .decorators import admin_required
import pandas as pd
from django.conf import settings
import os
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.contrib.admin.models import LogEntry
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test              
#from django.http import HttpResponse

# Create your views here.
def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def index(request):
    return render(request,'index.html')

@login_required
def comges(request):
    return render(request,'comges.html')

@login_required
def gestionclinica(request):
    return render(request,'gestionclinica.html')

@login_required
def glosa(request):
    return render(request,'glosa.html')

@login_required
def iaaps(request):
    return render(request,'iaaps.html')

@login_required
def metasanitarias(request):
    return render(request,'metasanitarias.html')

@login_required
def intranet(request):
    return render(request, 'intranet.html')  

@login_required
def LoginView(request):
    return render(request, 'login.html')

@login_required
def admin_panel(request):
    return render(request, 'admin/admin_panel.html')

@login_required
def LogoutView(request):
    user = request.user
    logout(request)
    LogEntry.objects.log_action(
        user_id=user.pk,
        content_type_id=ContentType.objects.get_for_model(user).pk,
        object_id=user.pk,
        object_repr=str(user),
        action_flag=2,  # 2 corresponde a “logout” en el Log de Django
        change_message='Cierre de sesión exitoso'  # Mensaje personalizado de cierre de sesión
    )
    return redirect('logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def powerbi_config(request):
    # Aquí iría la lógica para manejar la configuración de Power BI
    if request.method == 'POST':
        embed_url = request.POST.get('embed_url')
        client_id = request.POST.get('client_id')
        if embed_url and client_id:
            # Guardar la configuración en el archivo de configuración o base de datos
            settings.POWER_BI_EMBED_URL = embed_url
            settings.POWER_BI_CLIENT_ID = client_id
            messages.success(request, 'Configuración de Power BI guardada exitosamente.')
        else:
            messages.error(request, 'Por favor, complete todos los campos.')
    return render(request, 'admin/powerbi_config.html')

def excel_manager(request):
    # Aquí iría la lógica para manejar la carga y descarga de archivos Excel
    if request.method == 'POST':
        file = request.FILES.get('excel_file')
        if file:
            try:
                save_path = os.path.join(settings.MEDIA_ROOT, 'admin', 'excel', file.name)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, 'wb+') as dest:
                    for chunk in file.chunks():
                        dest.write(chunk)
                # Aquí podrías procesar el archivo Excel si es necesario
                df = pd.read_excel(save_path)
                # Procesar el DataFrame df según sea necesario
                messages.success(request, 'Archivo Excel cargado exitosamente.')
            except Exception as e:
                messages.error(request, f'Error al cargar el archivo: {str(e)}'
                               )
    return render(request, 'admin/excel_manager.html')



def admin_check(user):
    return user.is_authenticated and user.is_data_admin


@login_required
def registro_usuario(request):
    if not request.user.es_creador:
        return redirect('acceso denegado')
    
    if request.method == 'POST':
        form = RegistroSeguroForm(request.POST, usuario_creador=request.user)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.creador = request.user
            usuario.save()

            return redirect('admin_panel')

    else:
        form = RegistroSeguroForm(usuario_creador=request.user)
    return render(request, 'registro_usuario.html', {'form': form})

@login_required
@permission_required('auth.change_user')
def asignar_creador(request, user_id):
    if not request.user.is_superuser:
        return redirect('acceso-denegado')
    
    usuario = get_object_or_404(registro_usuario, pk=user_id)
    usuario.es_creador = not usuario.es_creador
    usuario.save()
    
    action = "habilitado" if usuario.es_creador else "deshabilitado"
    messages.success(request, f'Usuario {action} como creador de cuentas')
    
    return redirect('admin:auth_user_changelist')  # O tu vista personalizada