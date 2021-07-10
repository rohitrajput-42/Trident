from django.db import models

class Item(models.Model):

    Name = models.CharField(max_length = 400)
    Weight = models.DecimalField(max_digits = 10, decimal_places = 2)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name