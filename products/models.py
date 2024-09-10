from django.db import models


class Product(models.Model):
    """
    Модель продукта, содержащая информацию о названии, описании и цене
    продукта.
    """
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Возвращает строковое представление модели, которое будет отображаться
        в админке.
        """
        return self.name
