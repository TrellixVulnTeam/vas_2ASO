from django.db import models


class Otp(models.Model):
    otpId = models.CharField(max_length=30)
    statusId = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)

    def __str__(self):
        return self.otpId+'/'+self.statusId+'/'+self.recipient
