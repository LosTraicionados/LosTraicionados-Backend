from django.db import models

# Create your models here.
class Worker(models.Model):
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=100)
    post_id = models.IntegerField()
    post_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_name} ({self.post_name} en {self.company_name}'