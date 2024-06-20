from django.db import models

# Create your models here.
class Evaluation(models.Model):
    user_id = models.IntegerField()
    adaptability_to_change = models.FloatField()
    safe_conduct = models.FloatField()
    dynamism_energy = models.FloatField()
    personal_effectiveness = models.FloatField()
    initiative = models.FloatField()
    working_under_pressure = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f'Evaluation for User {self.user_id} on {self.date}'