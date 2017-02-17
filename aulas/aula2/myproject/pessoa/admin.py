from django.contrib import admin

# Register your models here.

from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco')
    list_filter = ['nome']
    search_fields = ['nome']

admin.site.register(Pessoa,PessoaAdmin)
