from django.shortcuts import render

#from django.views.generic import CreateView
from .models import Docente
from .models import DocenteImagem
from .forms import FormDocente, FormDocenteImagem  


def Formulario(request):
        if request.method == "POST":
            form_docente = FormDocente(request.POST)
            form_imagem = FormDocenteImagem(request.POST, request.FILES)
        
            if form_docente.is_valid() and form_imagem.is_valid():
                docente = form_docente.save()
                uploaded_images = request.FILES.getlist('imagens')
            
                for f in uploaded_images:
                    DocenteImagem.objects.create(docente=docente, imagem=f)
            return render(request, 'form-create.html', {'form_docente': FormDocente(), 'form_imagem': FormDocenteImagem()})
        else:
                form_docente = FormDocente()
                form_imagem = FormDocenteImagem()

        return render(request, 'form-create.html', {'form_docente': form_docente, 'form_imagem': form_imagem})
