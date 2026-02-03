from django.db import models

# Create your models here.
from django.db import models

class Admin(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Staff', 'Staff'),
    ]
    Username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)
    Role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.Username


class Customer(models.Model):
    Custid = models.IntegerField(primary_key=True)
    Accno = models.IntegerField(unique=True)
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Dob = models.CharField(max_length=20)
    Phno = models.BigIntegerField()
    Amount = models.FloatField()

    def __str__(self):
        return f"{self.Name} - {self.Accno}"


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('d', 'Deposit'),
        ('w', 'Withdraw'),
    ]
    Date = models.DateTimeField()
    Accno = models.IntegerField()
    Type = models.CharField(max_length=1, choices=TRANSACTION_TYPE)
    Amount = models.FloatField()

    def __str__(self):
        return f"{self.Accno} - {self.Type}"