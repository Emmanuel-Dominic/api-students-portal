from django.db import models


# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", unique=True, max_length=60)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=7, choices=(('male', 'M'), ('female', 'F')))
    password = models.CharField(max_length=255)
    course = models.ForeignKey('courses.course', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email
