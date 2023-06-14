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
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, default='')
    link = models.URLField(blank=True, null=True)
    area = models.CharField(max_length=100, default='LifeStyle')
    likes = models.IntegerField(default=0)


    def __str__(self):
        return self.titulo

class Comentario(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
        autor = models.ForeignKey(Dono, on_delete=models.CASCADE)
        titulo = models.CharField(max_length=100)
        texto = models.TextField()

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
