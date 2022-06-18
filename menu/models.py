from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='カテゴリ')
    slug = models.SlugField(max_length=250, unique=True, primary_key=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'

    def __str__(self):
        return '{}'.format(self.name)
    
    
class SubCategory(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='サブカテゴリ')
    slug = models.SlugField(max_length=250, unique=True, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='カテゴリ')

    class Meta:
        ordering = ('name',)
        verbose_name = 'サブカテゴリ'
        verbose_name_plural = 'サブカテゴリ'

    def __str__(self):
        return '{}'.format(self.name)


class Menu(models.Model):
    name = models.CharField(max_length=250, unique=False, verbose_name='名前')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='カテゴリ')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='サブカテゴリ')
    image = models.ImageField(upload_to='menu', blank=False)
    price = models.IntegerField(blank=True, verbose_name='値段')
    available = models.BooleanField(default=True, verbose_name='公開')
    

    class Meta:
        db_table = 'menu'
        ordering = ('name',)
        verbose_name = 'メニュー'
        verbose_name_plural = 'メニュー'

    
    def __str__(self):
        return '{}'.format(self.name)