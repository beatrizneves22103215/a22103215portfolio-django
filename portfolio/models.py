from datetime import timezone

from django.utils import timezone



from django.db import models


class Dono(models.Model):
    nome = models.CharField(max_length=100, default='Desconhecido')
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Post(models.Model):
    autor = models.CharField(max_length=100, default='Desconhecido')
    data = models.DateField(default=timezone.now())
    titulo = models.CharField(max_length=100,default='Nenhuma descrição')
    descricao = models.CharField(max_length=100, default='')
    link = models.URLField(blank=True, null=True)
    area = models.CharField(max_length=100, default='LifeStyle')
    likes = models.IntegerField(default=0)



    def __str__(self):
        return self.titulo



class Projeto(models.Model):
        projeto = models.CharField(max_length=100)
        nome = models.CharField(max_length=100)
        orientador = models.CharField(max_length=100)
        resumo = models.TextField()
        link1 = models.URLField()
        link2 = models.URLField()

        def __str__(self):
            return self.projeto



class laboratorios(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    lab = models.URLField()

    def __str__(self):
        return  self.titulo

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pagina_lusofona = models.URLField(blank=True)
    pagina_linkedin = models.URLField(blank=True)

class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    ano_letivo_frequentado = models.PositiveIntegerField()
    topicos_abordados = models.TextField(blank=True)
    professores = models.ManyToManyField(Pessoa, related_name='cadeiras',  blank=True)

    def __str__(self):
        return self.nome