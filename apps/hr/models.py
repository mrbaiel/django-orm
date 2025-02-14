from tkinter.constants import CASCADE

from django.contrib.postgres.indexes import HashIndex
from django.db import models



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


class CustomManager(models.Manager):
    def get_name(self):
        return self.values_list('first_name', flat=True)


class Employee(models.Model):
    first_name = models.CharField(verbose_name='Name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    about = models.CharField(verbose_name='About employee', max_length=500, null=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        indexes = (
            HashIndex(
                fields=('about',),
                name="hr_%(class)s_about_ix",
            ),
        )