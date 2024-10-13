from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):  # Use singular for the class name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')  # Optionally add related_name
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
