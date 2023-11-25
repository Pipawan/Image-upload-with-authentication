from django.db import models


class Image(models.Model):
    caption = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption


class IPAddress(models.Model):
    ip = models.GenericIPAddressField(unique=True)

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
