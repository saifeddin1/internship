from django.db import models

# Create your models here.

class Entreprise(models.Model):
    title = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    tel1 = models.BigIntegerField(default="")
    address = models.TextField()
    cadre = models.CharField(max_length=200)
    rib = models.TextField()
    description = models.TextField()      
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)
    marketing = models.ForeignKey('Marketing', on_delete=models.CASCADE)
    development = models.ForeignKey('Development', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel = models.FloatField()
    level = models.CharField(max_length=50)
    address = models.TextField()
    description = models.TextField()      
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)
    marketing = models.ForeignKey('Marketing', on_delete=models.CASCADE)
    development = models.ForeignKey('Development',on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Formation(models.Model):
    duration = models.BigIntegerField()
    domain = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    price = models.BigIntegerField()
    description = models.TextField()      

    def __str__(self):
        return self.domain

class Marketing(models.Model):
    product = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    duration = models.BigIntegerField()
    marketing_type = models.CharField(max_length=50)
    description = models.TextField()      

    def __str__(self):
        return self.title


class Development(models.Model):
    title = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    responsable = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)   
    duration = models.BigIntegerField()

    def __str__(self):
        return self.title


        