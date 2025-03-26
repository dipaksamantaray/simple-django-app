from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mob = models.CharField(max_length=11)
    password = models.CharField(max_length=8)
    # date = models.DateField()
    def __str__(self):
        return self.name
    