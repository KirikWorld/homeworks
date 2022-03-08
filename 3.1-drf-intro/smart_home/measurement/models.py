from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensors(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    describe = models.CharField(
        max_length=50, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик температуры'
        verbose_name_plural = 'Датчики температуры'

    def __str__(self):
        return self.name


class Measurment(models.Model):
    sensor = models.ForeignKey(
        Sensors, on_delete=models.CASCADE, verbose_name='ID датчика', related_name='measurements')
    temperature = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name='Температура')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Замер температуры'
        verbose_name_plural = 'Замеры температуры'

    def __str__(self):
        return f'{self.sensor_id}\nТемпература: {self.temperature}\nДата измерения: {self.date}'
