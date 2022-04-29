from django.db import models

# Create your models here.
class Predpriyatie(models.Model):
    bin_id = models.CharField(primary_key=True, max_length=12, unique=True, blank=False, verbose_name="БИН")
    full_name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Полное наименование")
    address = models.CharField(max_length=60, blank=False, unique=True, verbose_name="Адрес")
    phone = models.CharField(max_length=11, unique=True, blank=False, verbose_name="Телефон")
    fio_ruk = models.CharField(max_length=50, blank=False, unique=True, verbose_name="ФИО руководителя")
    uchrediteli = models.CharField(max_length=200, unique=True, verbose_name="Учредители")
    history = models.TextField(verbose_name="История")
    link = models.CharField(max_length=200, blank=False, unique=True, verbose_name="Сайт")

    def __str__(self):
        return f"{self.bin_id}, {self.full_name}"

    class Meta:
        verbose_name_plural = "Предприятия"


class Tag(models.Model):
    tag = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self):
        return f"{self.tag}"


class News(models.Model):
    bin_news = models.ForeignKey(Predpriyatie, on_delete=models.CASCADE, verbose_name="БИН предприятия")
    title = models.CharField(max_length=100, verbose_name="Тема")
    content = models.TextField(verbose_name="Описание")
    tags = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE, related_name='tags', verbose_name='Теги')
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return f"{self.bin_news}, {self.title}"

    class Meta:
        verbose_name_plural = "Новости"


class Comment(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='имя пользователя')
    text = models.CharField(max_length=5000, verbose_name='текст комментария')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news', verbose_name='Новость')

    def __str__(self):
        return f'{self.username}, {self.text}, {self.news}'