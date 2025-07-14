from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, default="")  # Allow blank and set default

    def __str__(self):
        return self.title
