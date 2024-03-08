from django.db import models

# Create your models here.
class ThemesSiteSetting(models.Model):
    banner = models.ImageField(upload_to='uploads/site')
    caption = models.TextField()