from django import forms

class contactForm(forms.Form):
    """contactForm definition."""

    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput( #? Extrayendo un textinput de forms
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre...'} 
        #? Practicamente son los atributos que modificariamos en el html solo que de esta forma django lo hace por nosotros
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email...'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu mensaje...'}
    ), min_length=10, max_length=1000)

