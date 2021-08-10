from django.db import models


class Instruction(models.Model):
    operation = models.PositiveIntegerField()
    number = models.CharField(max_length=50)
    version = models.CharField(max_length=12)
    title = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to='pdf_files/')

    def __str__(self):
        return f'{self.operation} - {self.title}  --- ред.{self.version}'

    def number_instruction(self):
        pass

    class Meta:
        verbose_name = "Рабочая инструкция"
        verbose_name_plural = "Рабочие инструкции"


class Manual(models.Model):
    operation = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to='pdf_files/')

    def __str__(self):
        return f'{self.operation} - {self.title}'

    class Meta:
        verbose_name = "Мануал"
        verbose_name_plural = "Мануалы"


class Circuit(models.Model):
    operation = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to='pdf_files/')

    def __str__(self):
        return f'{self.operation} - {self.title}'

    class Meta:
        verbose_name = "Электрическая схема"
        verbose_name_plural = "Электрические схемы"


class Catalog(models.Model):
    operation = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to='pdf_files/')

    def __str__(self):
        return f'{self.operation} - {self.title}'

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"
