from django.db import models


class OnePixel(models.Model):
    name_of_PC = models.CharField(max_length=255, verbose_name="Имя компьютера")
    FirstCoordinate = models.IntegerField(verbose_name="Первая координата")
    SecondCoordinate = models.IntegerField(verbose_name="Вторая координата")
    PixelColor = models.CharField(max_length=7, verbose_name="Цвет", default="#ffffff")

    def __str__(self):
        return self.name_of_PC + ", " + self.PixelColor + "(" + str(self.FirstCoordinate) + "," + str(self.SecondCoordinate) + ")"
