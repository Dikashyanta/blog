from django.db import models

# Create your models here.
class About(models.Model):
    about_heding = models.CharField(max_length=200)
    about_description = models.TextField(max_length=7000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heding