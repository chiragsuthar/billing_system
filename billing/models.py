from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Bill(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total_cost(self):
        return sum(item.price for item in self.items.all())

    def save(self, *args, **kwargs):
        if not self.id:  # Check if the bill is being saved for the first time
            super().save(*args, **kwargs)  # Save the bill to get an ID
            self.total_cost = self.calculate_total_cost()  # Calculate total cost
            super().save(*args, **kwargs)  # Save the bill again with updated total cost
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.pk}"
