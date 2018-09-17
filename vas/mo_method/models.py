from django.db import models


class Mo(models.Model):
    text = models.CharField(max_length=30)
    fromKey = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    smsId = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)

    def __str__(self):
        return self.text
