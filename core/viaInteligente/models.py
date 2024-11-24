from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    # Nome do status (Ex: Pendente, Aprovado, Rejeitado)
    nome = models.CharField(max_length=50, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='status_criados'
    )
    modificado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='status_modificados',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if 'modificado_por' in kwargs:
            self.modificado_por = kwargs.pop('modificado_por')
        super().save(*args, **kwargs)


class Acidente(models.Model):
    descricao = models.TextField()
    imagem_base64 = models.TextField()
    localizacao = models.CharField(max_length=255)
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        related_name='acidentes'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='acidentes_criados'
    )
    modificado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='acidentes_modificados',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = Status.objects.get(nome='Pendente')

        if 'modificado_por' in kwargs:
            self.modificado_por = kwargs.pop('modificado_por')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Acidente {self.id} - {self.status.nome if self.status else 'Sem status'}"
