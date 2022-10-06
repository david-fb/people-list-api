from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    document_type= models.CharField(max_length=5)
    document= models.BigIntegerField(unique=True)
    names= models.CharField(max_length=60)
    surnames= models.CharField(max_length=60)
    hobbie= models.CharField(max_length=30)