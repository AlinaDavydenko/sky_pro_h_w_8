from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    picture = models.ImageField(upload_to='materials/course_picture', blank=True, null=True, verbose_name='Картинка')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    picture = models.ImageField(upload_to='materials/lesson_picture', blank=True, null=True, verbose_name='Картинка')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    video_link = models.TextField(blank=True, null=True, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Курс',
                               help_text='Выберите курс')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
