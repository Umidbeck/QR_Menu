from django.db import models
from django.contrib.auth.models import AbstractUser
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория номи")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", help_text="URL uchun foydalaniladi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Яратилган сана")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Янгиланган сана")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категориялар"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Маҳсулот номи")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Нарx")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Расм")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug", help_text="URL uchun foydalaniladi")
    is_available = models.BooleanField(default=True, verbose_name="Мавjudлик")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Яратилган сана")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Янгиланган сана")

    class Meta:
        verbose_name = "Маҳсулот"
        verbose_name_plural = "Маҳсулотлар"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.category.name}) - {self.price} сум"
    
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=True, verbose_name="Админ ҳуқуқи")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон рақам")

    # related_name qo'shish
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Noyob nom
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Noyob nom
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
