from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    isbn=models.CharField(max_length=255, blank=True, null=True)
    publisher=models.CharField(max_length=255, blank=True, null=True)
    pages=models.IntegerField(default=0)
    stock=models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    outstanding_debt=models.DecimalField(max_digits=8,decimal_places=2,default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    issue_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(blank=True, null=True)
    returned=models.BooleanField(default=False)
    rent_fee=models.DecimalField(max_digits=6, decimal_places=2, default=0)