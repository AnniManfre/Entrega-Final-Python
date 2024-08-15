from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from Proyecto.models import DatosAlmacenados

class IngresarDatosForm(forms.ModelForm):
    class Meta:
        model = DatosAlmacenados
        fields = ['date', 'weight', 'waist', 'hips', 'neck', 'energy_level']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': _('Ingrese la fecha (YYYY-MM-DD)')}),
            'weight': forms.NumberInput(attrs={'placeholder': _('Peso (kg)')}),
            'waist': forms.NumberInput(attrs={'placeholder': _('Cintura (cm)')}),
            'hips': forms.NumberInput(attrs={'placeholder': _('Cadera (cm)')}),
            'neck': forms.NumberInput(attrs={'placeholder': _('Cuello (cm)')}),
            'energy_level': forms.NumberInput(attrs={'placeholder': _('Nivel de Energía (1-10)')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']

    def clean_energy_level(self):
        energy_level = self.cleaned_data.get('energy_level')
        
        if energy_level < 1 or energy_level > 10:
            raise ValidationError(_("El nivel de energía debe ser un número entre 1 y 10."))
        
        return energy_level

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            return HttpResponseRedirect(reverse('Ver Datos'))
        else:
            return instance

