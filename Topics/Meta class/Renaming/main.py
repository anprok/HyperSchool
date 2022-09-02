from django.db import models


class Mouse(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'mouse'
        verbose_name_plural = 'mice'
