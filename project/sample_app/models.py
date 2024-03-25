from django.core.cache import cache


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):
        return f'/products/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')