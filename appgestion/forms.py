from django import forms
from django.contrib.auth.forms import UserCreationForm
from appgestion.models import CustomUser

class RegistroSeguroForm(UserCreationForm):
    codigo_creador = forms.CharField(
        label='Código del creador',
        widget=forms.PasswordInput,
        required=True,
        help_text='Códgigo especial proporcionado por el administrador'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'rut', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario_creador = kwargs.pop('usuario_creador', None)
        super().__init__(*args, **kwargs)

    def clean_codigo_creador(self):
        codigo = self.cleaned_data.get('codigo_creador')
        if not self.usuario_creador or not self.usuario_creador.es_creador:
            raise forms.ValidationError('No tienes permiso para crear cuentas.')
        
        if codigo != "CLAVE_SEGURA":
            raise forms.ValidationError('Clave de creador incorrecto.')
        return codigo    
        