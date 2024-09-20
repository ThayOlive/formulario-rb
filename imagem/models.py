from django.db import models
from datetime import time

class Docente(models.Model):
    SITUACAO_CHOICES = [
        ('formacao', 'Formação'),
        ('reciclagem', 'Reciclagem'),
        ('complementacao', 'Complementação'),
    ]

    nome = models.CharField(max_length=100, blank=False, null=False, default="Docente")
    turno = models.CharField(max_length=30, blank=False, null=False, default="Informe o turno, manha/tarde/noite")
    cod_treinamento = models.IntegerField(null=False, blank=False, help_text="Inserir o número do código", default=0)
    situacao = models.CharField(max_length=50, choices=SITUACAO_CHOICES, default='formacao', help_text="Formação, reciclagem ou complementação")
    carga_horaria = models.TimeField(default=time(0, 0), blank=False, null=False)
    quantidade_alunos = models.IntegerField(null=False, blank=False, default=0)
    data_inicio = models.DateField(null=True, blank=True)
    data_termino = models.DateField(null=True, blank=True)
    cliente = models.CharField(max_length=200, blank=False, default="Cliente não informado")
    aula_pratica = models.CharField(max_length=50, null=True, blank=True)
    dificuldades = models.TextField( blank=True, help_text="Descreva as dificuldades encontradas no treinamento")
    treinamento_requisitos = models.TextField(help_text="Equipamentos e/ou processos que necessitam ser implementados para que os funcionários tenham êxito em suas atividades", blank=True)
    observacoes = models.TextField(help_text="Descreva qualquer observação ocorrida no treinamento, atrasos, colaboradores que não concluíram o treinamento, não realizaram aula prática, etc", blank=True)
    critica_elogio = models.TextField(help_text="Deixe uma crítica / elogio para que possa haver melhoria contínua", blank=True)

    def __str__(self):
        return self.nome

class DocenteImagem(models.Model):
    imagem = models.FileField(upload_to='imagens')
    docente = models.ForeignKey(Docente, related_name='imagens', on_delete=models.CASCADE)

    def __str__(self):
        return self.docente.nome