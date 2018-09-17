from django.db import models


class Sub(models.Model):
    text = models.CharField(max_length=30)
    keyword = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    fromKey = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    NotificationId = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)


    def __str__(self):
        return self.text
