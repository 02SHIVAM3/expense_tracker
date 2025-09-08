from django.db import models

# Create your models here.

class UserDetail(models.Model):
    FullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    password = models.CharField(max_length=50)
    RegDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    UserId = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    expenseDate = models.DateField()
    ExpenseItem = models.CharField(max_length=50)
    amount = models.FloatField()
    Notedate = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"{self.user.FullName} - {self.amount} on {self.date}"