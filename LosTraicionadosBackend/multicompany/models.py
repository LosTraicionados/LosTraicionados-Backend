from django.db import models

# Create your models here.
class MultiCompany(models.Model):
    main_company_id = models.IntegerField()
    sub_company_id = models.IntegerField()
    main_company_name = models.CharField(max_length=100)
    sub_company_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.main_company_name} - {self.sub_company_name}'