from django.db import models


class File(models.Model):
    name = models.TextField()
    size = models.IntegerField()
    extension = models.TextField()
    catalog = models.ForeignKey("Catalog", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.TextField()
