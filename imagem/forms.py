from django import forms
from .models import Docente, DocenteImagem
    
class FormDocente(forms.ModelForm):
      
    class Meta:
        model= Docente
        fields= ['nome','turno','cod_treinamento','situacao','carga_horaria','quantidade_alunos','data_inicio','data_termino','cliente','aula_pratica','dificuldades','treinamento_requisitos','observacoes','critica_elogio']

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        print(self.fields.items())
        for field_name, field in self.fields.items():
            field.widget.attrs['class']= 'form-control'


class MultipleFileInput(forms.ClearableFileInput):
                allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        kwargs.setdefault("required", False)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if isinstance(data, list):
              return [super().clean(d, initial) for d in data]
        return super().clean(data, initial)
    
class FormDocenteImagem(forms.Form):
        imagens = MultipleFileField(label='Select files', required=False)
       

   
