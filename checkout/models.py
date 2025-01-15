from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=1, unique=True, help_text="Single character item identifier (e.g., A, B).")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of a single item.")
    special_quantity = models.PositiveIntegerField(null=True, blank=True, help_text="Quantity for special price.")
    special_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Special price for the specified quantity.")

    def __str__(self):
        return self.name
