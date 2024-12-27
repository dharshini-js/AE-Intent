from django.db import models

class Admin(models.Model):
    admin_name = models.CharField(max_length=50, null=False, blank=False)
    password=models.CharField(max_length=50, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.admin_name




class Employee(models.Model):
    emp_id=models.IntegerField(null=False, blank=False, unique=True)
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    mob_num = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    user_password=models.CharField(max_length=50, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.emp_name
