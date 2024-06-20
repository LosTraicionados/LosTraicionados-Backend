from django.db import models

# Create your models here.
class worker(models.Model):
    EVALUADO = 'evaluado'
    INTERVENCION = 'intervencion'
    NO_INTERVENIDO = 'no intervenido'

    STATE_CHOICES = [
        (EVALUADO, 'Evaluado'),
        (INTERVENCION, 'Intervención'),
        (NO_INTERVENIDO, 'No Intervenido'),
    ]
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=100)
    post_id = models.IntegerField()
    post_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    state = models.CharField(
        max_length=15,
        choices=STATE_CHOICES,
        default=EVALUADO,
    )

    def __str__(self):
        return f'{self.user_name} ({self.post_name} en {self.company_name})'