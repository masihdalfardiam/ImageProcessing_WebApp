from django.db import models
from django.contrib.auth.models import User

class UploadedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text1 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    text_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'dashboard'

    def __str__(self):
        return f"Data for {self.user.username}"
