from django.db import models

class Orcamento(models.Model):
    nome_completo = models.CharField(max_length=255)
    nome_artistico = models.CharField(max_length=255, blank=True, null=True)
    cidade_estado = models.CharField(max_length=255)
    email = models.EmailField()
    instagram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255)
    genero_musical = models.CharField(max_length=255, blank=True, null=True)
    beat_exclusivo = models.BooleanField(default=False)
    composicao = models.BooleanField(default=False)
    captacao_voz = models.BooleanField(default=False)
    mixagem_masterizacao = models.BooleanField(default=False)
    identidade_visual = models.BooleanField(default=False)
    mensagem = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo
