from django.db import models

# Create your models here.
class MarkList(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    marks_math = models.DecimalField(max_digits=5, decimal_places=2)
    marks_science = models.DecimalField(max_digits=5, decimal_places=2)
    marks_english = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
