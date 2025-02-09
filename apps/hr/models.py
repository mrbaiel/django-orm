from tkinter.constants import CASCADE

from django.db import models

class Compensation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    phone = models.CharField(max_length=10, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name="email", null=True)
    address = models.CharField(max_length=100, verbose_name='адрес')

    def __str__(self):
        return f"email: {self.email}"


class Department(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)
    description = models.TextField(verbose_name='description', null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(verbose_name='Name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    compensation = models.ManyToManyField(Compensation)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
