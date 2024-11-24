from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    # Nome do status (Ex: Pendente, Aprovado, Rejeitado)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Acidente(models.Model):
    descricao = models.TextField()
    imagem_base64 = models.TextField()
    localizacao = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        related_name='acidentes',
        default=None
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='acidentes'
    )

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = Status.objects.get(nome='Pendente')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Acidente {self.id} - {self.status.nome if self.status else 'Sem status'}"
