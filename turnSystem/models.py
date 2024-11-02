from django.db import models


class Turn(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"Turno de {self.usuario.username} - {'Atendido' if self.atendido else 'Pendiente'}"
