from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(null=True, max_length=100)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exist = models.BooleanField(null=True)
    slug = models.SlugField(null=True, max_length=100)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exist}, {self.slug}'
