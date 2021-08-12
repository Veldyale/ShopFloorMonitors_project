from django.db import models


class Item(models.Model):
    baan_id = models.CharField(max_length=50, unique=False)
    title = models.CharField(max_length=50, blank=False)
    item_name = models.CharField(max_length=50, blank=True)
    screw_thread = models.CharField(max_length=5, blank=True)
    diameter = models.PositiveIntegerField(blank=True)
    length = models.PositiveIntegerField(blank=True)
    height = models.PositiveIntegerField(blank=True)
    strength = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    iso = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=10, blank=True)
    assembly_place = models.CharField(max_length=10, unique=True, blank=False)
    warehouse_place = models.CharField(max_length=10)
    file = models.FileField(upload_to='images/', blank=True)

    def __str__(self):
        return f'id {self.baan_id}  Винт  {self.screw_thread}  {self.diameter}  {self.length}  {self.strength}  {self.assembly_place}'

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"