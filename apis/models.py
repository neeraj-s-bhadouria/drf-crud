from django.db import models


class Students(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField(max_length=2)
    standard = models.IntegerField(max_length=2)
    roll_number = models.IntegerField(max_length=5)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Students'