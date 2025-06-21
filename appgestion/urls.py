from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import excel_manager , powerbi_config
urlpatterns = [
    
    
    path('', index, name='index'),
    path('comges/', views.comges, name='comges'),
    path('gestionclinica/', views.gestionclinica, name='gestionclinica'),
    path('glosa/', views.glosa, name='glosa'),
    path('iaaps/', views.iaaps, name='iaaps'),
    path('metasanitarias/', views.metasanitarias, name='metasanitarias'),
    path('intranet/', views.intranet, name='intranet'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('excel_manager/', excel_manager, name='excel_manager'),
    path('powerbi_config/', powerbi_config, name='powerbi_config'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
