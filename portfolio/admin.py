from django.contrib import admin
from .models import Post, Projeto, laboratorios, Cadeira

# Register your models here.

admin.site.register(Post)
admin.site.register(Projeto)
admin.site.register(laboratorios)
admin.site.register(Cadeira)
