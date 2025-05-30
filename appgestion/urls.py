from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    
    
    path('', index, name='index'),
    path('comges/', views.comges, name='comges'),
    path('gestionclinica/', views.gestionclinica, name='gestionclinica'),
    path('glosa/', views.glosa, name='glosa'),
    path('iaaps/', views.iaaps, name='iaaps'),
    path('metasanitarias/', views.metasanitarias, name='metasanitarias'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
