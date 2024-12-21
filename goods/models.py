from django.db import models

class Categorys(models.Model):
    name=models.CharField(max_length=100, verbose_name='Название категории', unique=True)
    slug=models.SlugField(max_length=100, verbose_name='URL', unique=True)

    class Meta:
        db_table="categorys"
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return self.name

class Products(models.Model):
    title=models.CharField(max_length=100, verbose_name='Название продукта', unique=True)
    description=models.TextField(blank=True, null=True, verbose_name='Описание')
    slug=models.SlugField(max_length=100, verbose_name='URL', unique=True)
    image=models.ImageField(upload_to='media', blank=True, null=True, verbose_name='Изображение')
    price=models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount=models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quatity=models.PositiveIntegerField(default=0, verbose_name='Количество')
    category=models.ForeignKey(to=Categorys, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table='products'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        ordering=("id",)

    def __str__(self):
        return f'{self.title} Количество - {self.quatity}'

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount / 100,2)
        return self.price
