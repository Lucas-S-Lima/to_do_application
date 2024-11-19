from django.db import models
from datetime import date


class Todo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    created_at = models.DateField(verbose_name="Criado em", auto_now_add=True, null=False, blank=False)
    finished_at = models.DateField(verbose_name="Entregue em", null=True)
    deadline = models.DateField(verbose_name="Data final", null=False, blank=False)

    class Meta:
        ordering = ["deadline"]

    def if_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.finished_at.save() 
