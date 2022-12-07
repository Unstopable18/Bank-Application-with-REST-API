from django.db import models

# Create your models here.
class AccountType(models.Model):
    acType=models.CharField(max_length=100)

    def __str__(self):
        return self.acType

class Account(models.Model):
    acno=models.PositiveBigIntegerField()
    name=models.CharField(max_length=200)
    dob=models.DateField()
    aadhar=models.PositiveBigIntegerField()
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=64)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)
    balance=models.PositiveIntegerField()
    actype=models.ForeignKey(AccountType,on_delete=models.CASCADE)


