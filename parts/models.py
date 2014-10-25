from django.db import models

class Part(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    part_number = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        items = [str(self.serial_number), str(self.part_number),\
                str(self.price), str(self.quantity), self.location]
        item_string = '\t'.join(items)
        return item_string
    