from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings

# Create your models here.


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Укажите почту')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон', help_text='Укажите телефон')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город', help_text='Укажите город')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey('courses.Lesson', on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Оплаченный урок')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ['-payment_date']

    def __str__(self):
        return f'Платеж {self.user.email} на сумму {self.amount}'
