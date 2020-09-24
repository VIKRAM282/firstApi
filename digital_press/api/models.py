from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneno = models.IntegerField()
    rollno = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class meta:
        db_table = "student"