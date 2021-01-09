from django.db import models

# Create your models here.

class Kwic(models.Model):
    content = models.TextField(verbose_name='输入内容')
    result = models.TextField(verbose_name='处理结果')

    class Meta:
        verbose_name = 'KWIC处理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)