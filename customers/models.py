from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
            email = models.EmailField()
                phone = models.CharField(max_length=20)
                    address = models.TextField()

                        def __str__(self):
                                return f"{self.first_name} {self.last_name}"
                                