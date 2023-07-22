from django.db import models

# Create your models here.
SEX = (('female', 'Female'), ('male', 'Male'))
class Customer(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(choices=SEX, max_length=255 )
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name