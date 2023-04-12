from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage #? Sirve para crear la estructura de un mensaje e incluye un metodo para enviarlo
from .forms import contactForm

# Create your views here.
def contact(request):
    contact_form = contactForm() #* Instanciando contact_form

    if request.method == "POST": #? Si se envia algo por el metodo POST 
        contact_form = contactForm(data=request.POST)
        #? Vamos a instanciar el objeto y pasarle el diccionario que se recoge del formulario que genero el post
        
        if contact_form.is_valid(): #? Si el formulario es valido entonces...
            name = request.POST.get('name', '') #? vamos a obtener el valor del diccionario en la calve name sino que nos devuelva una cadena vacia
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            #* Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #? Asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content), #? Cuerpo 
                #? .format es para indicarle el orden de las variables y su contenido, que van en los espacios que dejamos con llaves
                "no-contestar@inbox.mailtrap.io", #? email_origen
                ["samuel009godoy@gmail.com"],  #? email_destino
                reply_to=[email]
            )

            try:
                email.send()
                #? Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")  #? reverse es un template tag url para no poner la url en crudo y que django la procese              
            except:
                #! Algo no ha ido bien, redirrecionamos a FAIL
                return redirect(reverse('contact'+"?fail"))

            
    return render(request, "contact/contact.html", {'form': contact_form}) #* Pasando la instancia como parametro para poder recogerlo en el template