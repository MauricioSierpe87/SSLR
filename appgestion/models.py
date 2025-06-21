from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class CustomUser(AbstractUser):
    """Modelo de usuario personalizado que extiende AbstractUser
    para incluir campos adicionales específicos de la aplicación."""
    is_data_admin = models.BooleanField(
        'administrador de datos',
        default=False,
        help_text='Puede gestionar Excel y Power BI'
    )

    is_account_creator = models.BooleanField(
        'creador de cuentas',
        default=False,
        help_text='Puede crear cuentas de usuario'
    )

    rut = models.CharField(
        'RUT',
        max_length=12,
        unique=True,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^0*(\d{1,3}(\.?\d{3})*\-?[\dkK])$',
            message='Ingrese un RUT válido (ej: 12345678-9)'
        )]
    )

    create_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_users',
        verbose_name='creado por',
        help_text='Usuario que creó esta cuenta'
    )

    # Audotoría
    ip_register = models.GenericIPAddressField(
        'IP de registro',
        null=True,
        blank=True,
        
    )

    Device_register = models.CharField(
        'Dispositivo de registro',
        max_length=255,
        null=True,
        blank=True,
        
    )

    

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"
    
    @property
    def can_create_account(self):
        """Verifica si el usuario tiene permiso para crear cuentas."""
        return self.is_superuser or self.is_account_creator

AUTH_USER_MODEL = 'appgestion.CustomUser'